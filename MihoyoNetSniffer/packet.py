import traceback
from pathlib import Path
from logging import getLogger
from dataclasses import dataclass
from enum import IntEnum
from queue import SimpleQueue
from threading import Thread, Event
from win32file import ReadFile
from win32pipe import CreateNamedPipe, ConnectNamedPipe, DisconnectNamedPipe, PIPE_ACCESS_DUPLEX, PIPE_TYPE_BYTE, \
	PIPE_READMODE_BYTE, PIPE_WAIT
from pywintypes import error as win32_error
from .error import PipeError, FileEndError
logger = getLogger('MihoyoNetSniffer.Packet')
STOP_SIGNAL = -1


class PacketType(IntEnum):
	Null = 0
	PacketData = 1
	ModifyData = 2


class Direction(IntEnum):
	Send = 0
	Receive = 1


@dataclass
class RawPacket:
	packet_type: PacketType
	time_stamp: int
	manipulation_enabled: bool
	direction: Direction
	message_id: int
	header: bytes = b''
	content: bytes = b''


class PipePacketStream:
	def __init__(
			self,
			pipe_name='genshin_packet_pipe',
			dump_file: str or Path = None,
			dump_only_mode=False):

		# output pipe
		self._pipe = CreateNamedPipe(
			'\\\\.\\pipe\\' + pipe_name,
			PIPE_ACCESS_DUPLEX, PIPE_TYPE_BYTE | PIPE_READMODE_BYTE | PIPE_WAIT,
			1, 256 * 1024, 256 * 1024, 0xFFFF, None)

		if dump_file and dump_only_mode:
			self._network_receive_loop = None
		else:
			self._network_receive_queue = SimpleQueue()

		# thread
		self._running_event = Event()
		self.wait_for_connected = self._running_event.wait
		self._network_receive_loop = Thread(target=self._loop, daemon=True)
		self.status_sign = False

		# dump
		if dump_file:
			dump_file = Path(dump_file)
			logger.info(f'Enable dump: {dump_file.name}')
			self.dump_file = dump_file.open('wb', buffering=1048576)
		else:
			self.dump_file = None

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
			self._network_receive_queue.put(STOP_SIGNAL)


	def read(self, length):
		ret, data = ReadFile(self._pipe, length)
		if ret:
			raise PipeError(ret, data)
		if len(data) < length:
			raise FileEndError(length, len(data), None)
		if self.dump_file:
			self.dump_file.write(data)
		return data

	def get_dynamic_length_data(self):
		length = int.from_bytes(self.read(8), 'little')
		return self.read(length)

	def _loop(self):
		queue = self._network_receive_queue
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
				queue.put(STOP_SIGNAL)
				self._running_event.clear()
				if self.dump_file:
					self.dump_file.flush()
				return
			try:
				packet = RawPacket(
					packet_type=PacketType(int.from_bytes(self.read(4), 'little')),
					time_stamp=int.from_bytes(self.read(8), 'little'),
					manipulation_enabled=bool(self.read(1)),
					direction=Direction(int.from_bytes(self.read(4), 'little')),
					message_id=int.from_bytes(self.read(2), 'little'),
					header=self.get_dynamic_length_data(),
					content=self.get_dynamic_length_data()
				)
				# print(packet.message_id)
				queue.put(packet)
			except win32_error:
				traceback.print_exc()
				self.status_sign = False

	def get_packet(self):
		uid = self._network_receive_queue.get()
		if uid != STOP_SIGNAL:
			return uid

	def send_packet(self, raw_packet):
		# TODO 发送数据包
		pass

	def __del__(self):
		if self._network_receive_loop.is_alive():
			self.status_sign = False
			self._network_receive_loop.join(timeout=5)
		if self.dump_file:
			self.dump_file.close()


def load_from_dump(file_obj):
	def read(n):
		data = file_obj.read(n)
		if len(data) < n:
			raise FileEndError(n, len(data), file_obj)
		return data

	def get_dynamic_length_data():
		length = int.from_bytes(read(8), 'little')
		return read(length)

	from struct import Struct
	header = Struct('<IQ?IH')
	while True:
		try:
			tmp1 = header.unpack(read(header.size))
			yield RawPacket(
				*tmp1,
				get_dynamic_length_data(),
				get_dynamic_length_data()
			)
		except FileEndError:
			return
