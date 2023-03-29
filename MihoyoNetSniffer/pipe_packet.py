import traceback
from pathlib import Path
from logging import getLogger
from threading import Thread, Event
from queue import Queue
from struct import Struct
from win32pipe import CreateNamedPipe, ConnectNamedPipe, DisconnectNamedPipe, PIPE_ACCESS_DUPLEX, PIPE_TYPE_BYTE, \
	PIPE_READMODE_BYTE, PIPE_WAIT
from win32file import ReadFile, WriteFile
from pywintypes import error as win32_error
from .error import PipeReadError, FileEndError, PipeWriteError
from .data_type import RawPacketInfo, PacketType, ModifyPacketInfo, PipeHeader, ModifyType, DataclassIO, Direction
from .util import make_a_thread, main_dir
logger = getLogger('MihoyoNetSniffer.PipePacket')
STOP_SIGNAL = -1


def get_bytes(read_func):
	length = int.from_bytes(read_func(8), 'little')
	return read_func(length)


def write_bytes(write_func, data):
	write_func(len(data).to_bytes(8, 'little'))
	write_func(data)


class PipePacketStream:
	def __init__(self, pipe_name, packet_dump_output='', no_modify_func=None, modify_func=None):
		from pathlib import Path
		self._pipe_header = DataclassIO(PipeHeader, '<LQ', self._read, self._write)
		self._raw_packet_info = DataclassIO(RawPacketInfo, '<?LH', self._read, self._write)
		self._modify_packet_info = DataclassIO(ModifyPacketInfo, '<LL', self._read, self._write)
		if packet_dump_output:
			self._dump = PacketDump(packet_dump_output)
		self._unblock_func = no_modify_func
		self._modify_func = modify_func

	def get_packet(self):
		while True:
			pipe_header = self._pipe_header.read()
			raw_packet_info = self._raw_packet_info.read()
			header = self.get_dynamic_length_data()
			content = self.get_dynamic_length_data()
			if raw_packet_info.manipulation_enabled:
				# TODO 修改packet（需要配合sniffer）
				modify_type, content = self._modify_func(pipe_header.time_stamp, raw_packet_info.direction, raw_packet_info.message_id, header, content)
				modify_info = ModifyPacketInfo(modify_type, raw_packet_info.message_id)
				modify_pipe_header = pipe_header.copy()
				modify_pipe_header.packet_type = 2
				self._pipe_header.write(modify_pipe_header)
				self._modify_packet_info.write(modify_info)
				self.write_dynamic_data(header)
				self.write_dynamic_data(content)
			else:
				self._unblock_func(pipe_header.time_stamp, raw_packet_info.direction, raw_packet_info.message_id, header, content)

	def _read(self, length):
		if length > 0:
			ret, data = ReadFile(self._pipe, length)
			if ret:
				raise PipeReadError(ret, data)
			if len(data) < length:
				raise FileEndError(length, len(data), None)
			return data

	def _write(self, data):
		if data:
			ret, lens = WriteFile(self._pipe, data)
			if ret != 0:
				raise PipeWriteError(ret, lens)

	def get_dynamic_length_data(self):
		length = int.from_bytes(self._read(8), 'little')
		return self._read(length)

	def write_dynamic_data(self, data: bytes or bytearray):
		self._write(int.to_bytes(len(data), 8, 'little'))
		self._write(data)

	def __del__(self):
		if self._dump:
			self._dump.__del__()


class PacketDump:
	def __init__(self, output):
		from os.path import basename
		logger.info(f'Enable Dump: {basename(output)}')
		self._file = open(output, 'wb', buffering=1048576)
		self._queue = Queue()
		self._dump_loop_thread = make_a_thread(self._dump_loop, True)
		from time import time
		self.__start_timestamp = int(time() * 1000)

	def dump_packet(
			self,
			time_stamp: int,
			direction: Direction,
			header: bytes,
			content: bytes,
			modify_type:ModifyType = ModifyType.Unchanged,
			modified_content=b''):
		self._queue.put((time_stamp, direction.value, header, content, modify_type.value, modified_content))

	def _dump_loop(self):
		self._file.write(self.__start_timestamp.to_bytes(8, 'little'))
		while True:
			data = self._queue.get()
			if data == STOP_SIGNAL:
				break
			time_stamp, direction, header, content, modify_type, modified_content = data
			interval_time = time_stamp - self.__start_timestamp
			if interval_time > 0x1fffffff:
				raise OverflowError('dump时间过长')
			info_flags = modify_type << 30 + direction << 29 + interval_time
			self._file.write(info_flags.to_bytes(4, 'little'))
			self.write_dynamic_data(header, 2)
			self.write_dynamic_data(content, 4)
			if modified_content:
				self.write_dynamic_data(content, 4)
			self._file.flush()

	def write_dynamic_data(self, data: bytes or bytearray, lens):
		self._file.write(int.to_bytes(len(data), lens, 'little'))
		self._file.write(data)

	@property
	def name(self):
		return self._file.name

	def __del__(self):
		if self._dump_loop_thread.is_alive():
			self._queue.put(STOP_SIGNAL)
			self._dump_loop_thread.join(15)
		self._file.close()


class PipeMessage:
	def __init__(
			self,
			pipe_name='genshin_packet_pipe',
			dump_file: str or Path = None,
			modify_dump_file: str or Path = None,
			callback=None):

		# output pipe
		self._pipe = CreateNamedPipe(
			'\\\\.\\pipe\\' + pipe_name,
			PIPE_ACCESS_DUPLEX, PIPE_TYPE_BYTE | PIPE_READMODE_BYTE | PIPE_WAIT,
			1, 256 * 1024, 256 * 1024, 0xFFFF, None)

		self._callback = callback

		# thread
		self._running_event = Event()
		self.wait_for_connected = self._running_event.wait
		self._network_receive_loop = Thread(target=self._loop, daemon=True)
		self.status_sign = False

		# dump
		self._stream = PipePacketStream(self.read, self.write)

	def start(self):
		logger.debug('启动接收器')
		self.status_sign = True
		if self._network_receive_loop.is_alive() is False:
			self._network_receive_loop.start()
		logger.debug('启动成功')

	def stop(self):
		logger.debug('关闭接收器')
		self.status_sign = False
		if self._network_receive_loop.is_alive():
			self._network_receive_loop.join(timeout=10)
		logger.debug('关闭成功')
		running_flag = self._network_receive_loop.is_alive()
		if running_flag:
			if self._callback:
				self._callback(None)

	def read(self, length):
		if length > 0:
			ret, data = ReadFile(self._pipe, length)
			if ret:
				raise PipeReadError(ret, data)
			if len(data) < length:
				raise FileEndError(length, len(data), None)
			if self.dump_file:
				self.dump_file._write(data)
			return data

	def write(self, data):
		if data:
			ret, lens = WriteFile(self._pipe, data)
			if ret != 0:
				raise PipeWriteError(ret, lens)
			if self.modify_dump_file:
				self.modify_dump_file._write(data)

	def get_dynamic_length_data(self):
		length = int.from_bytes(self.read(8), 'little')
		return self.read(length)

	def _loop(self):


		try:
			logger.info(f'开始监听pipe...')
			ConnectNamedPipe(self._pipe, None)
		except BaseException:
			traceback.print_exc()
			self.status_sign = False
		logger.info('连接成功')
		self._running_event.set()

		while True:
			if self.status_sign is False:
				DisconnectNamedPipe(self._pipe)
				logger.info('断开连接')
				if self._callback:
					self._callback(None)
				self._running_event.clear()
				if self.dump_file:
					self.dump_file.flush()
				if self.modify_dump_file:
					self.modify_dump_file.flush()
				return

			try:
				pipe_header = pipe_header_struct._read(self.read)
				if pipe_header.packet_type != PacketType.PacketData:
					continue
				client_info = client_info_struct._read(self.read)
				raw_packet = packet_struct._read(self.read)

				if self._callback:
					ret = self._callback(
						pipe_header.time_stamp,
						client_info.manipulation_enabled,
						client_info.direction,
						raw_packet
					)
					if client_info.manipulation_enabled is False:
						continue

					pipe_header._write(self.write, (2, pipe_header.time_stamp))
					if isinstance(ret, bytes):
						self.write(int.to_bytes(2, 4, 'little'))
						packet_struct._write(self.write, (raw_packet.message_id, raw_packet.header, ret))
					else:
						self.write(int.to_bytes(ret, 4, 'little'))
						self.write(b'\x00' * 10)
			except win32_error:
				traceback.print_exc()
				self.status_sign = False

	def __del__(self):
		if self._network_receive_loop.is_alive():
			self.status_sign = False
			self._network_receive_loop.join(timeout=5)

		if self.dump_file:
			self.dump_file.close()
		if self.modify_dump_file:
			self.modify_dump_file.close()


def get_all_struct():
	pipe_header_struct = StreamStruct('<LQ', PipeHeader)
	client_info_struct = StreamStruct('<?L', ClientInfo)
	return pipe_header_struct, client_info_struct, PipePacketStream


def load_from_dump(file_obj):
	def read(n):
		data = file_obj._read(n)
		if len(data) < n:
			raise FileEndError(n, len(data), file_obj)
		return data

	from struct import Struct
	header = Struct('<IQ?IH')
	while True:
		try:
			tmp1 = header.unpack(read(header.size))
			yield RawPacket(
				*tmp1,
				get_bytes(read),
				get_bytes(read)
			)
		except FileEndError:
			return
