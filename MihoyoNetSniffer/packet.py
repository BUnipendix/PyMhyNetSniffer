import traceback
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
logger = getLogger('PipePacket')


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


class GameNetwork:
	def __init__(self, name, dump_file: str = None):
		self._pipe = CreateNamedPipe(
			'\\\\.\\pipe\\' + name,
			PIPE_ACCESS_DUPLEX, PIPE_TYPE_BYTE | PIPE_READMODE_BYTE | PIPE_WAIT,
			1, 256 * 1024, 256 * 1024, 0xFFFF, None)
		self._network_receive_queue = SimpleQueue()
		self._running_event = Event()
		self.wait_for_connected = self._running_event.wait
		self._network_receive_loop = Thread(target=self._loop)
		self.status_sign = False
		if dump_file:
			logger.info(f'Enable dump: {dump_file}')
			self.dump_file = open(dump_file, 'wb')
		else:
			self.dump_file = None

	# self.packets = []

	def start(self):
		logger.debug('启动接收器')
		self.status_sign = True
		if self._network_receive_loop.is_alive() is False:
			self._network_receive_loop.start()
		logger.debug('启动成功')

	def stop(self):
		logger.debug('手动关闭接收器')
		self.status_sign = False
		if self._network_receive_loop.is_alive():
			self._network_receive_loop.join()
		logger.debug('关闭成功')


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
			print('start listening...')
			ConnectNamedPipe(self._pipe, None)
		except BaseException:
			traceback.print_exc()
			self.status_sign = False
		print('Connected')
		self._running_event.set()
		while True:
			if self.status_sign is False:
				DisconnectNamedPipe(self._pipe)
				print('Disconnected')
				queue.put(-1)
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
		if uid != -1:
			return uid

	def send_packet(self, raw_packet):
		# TODO 发送数据包
		pass

	def __del__(self):
		logger.debug('回收实例')
		self.stop()
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
