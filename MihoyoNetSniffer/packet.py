import traceback
from dataclasses import dataclass
from enum import IntEnum
from os import PathLike
from queue import SimpleQueue
from threading import Thread

from win32file import ReadFile
from win32pipe import CreateNamedPipe, ConnectNamedPipe, DisconnectNamedPipe, PIPE_ACCESS_DUPLEX, PIPE_TYPE_BYTE, \
	PIPE_READMODE_BYTE, PIPE_WAIT


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
			1, 256 * 1024, 16, 0xFFFF, None)
		self._network_receive_queue = SimpleQueue()
		self._network_receive_loop = Thread(target=self._loop)
		self.status_sign = False
		if dump_file:
			self.dump_file = open(dump_file, 'wb')
		else:
			self.dump_file = None

	# self.packets = []

	def start(self):
		self.status_sign = True
		self._network_receive_loop.start()

	def stop(self):
		self.status_sign = False
		self._network_receive_loop.join()

	def read(self, length):
		ret, data = ReadFile(self._pipe, length)
		if ret:
			raise '读取错误：错误码：%s， data：%s' % (ret, data)
		if len(data) < length:
			raise f'错误长度：%s，%s' % (ret, data)
		if self.dump_file:
			self.dump_file.write(data)
		return data

	def get_dynamic_length_data(self):
		length = int.from_bytes(self.read(8), 'little')
		return self.read(length)

	def _loop(self):
		queue = self._network_receive_queue
		# packets = self.packets
		ConnectNamedPipe(self._pipe, None)
		print('连接成功')
		while True:
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
			except BaseException as e:
				print(e)
				print(traceback.print_exc())
				self.stop()
				return
			if self.status_sign is False:
				DisconnectNamedPipe(self._pipe)
				queue.put(-1)
				return
			queue.put(packet)

	# queue.put(len(packets))
	# packets.append(packet)

	def get_packet(self):
		uid = self._network_receive_queue.get()
		if uid != -1:
			return uid

	def send_packet(self, raw_packet):
		# TODO 发送数据包
		pass

	def __del__(self):
		self.stop()
		if self.dump_file:
			self.dump_file.close()


def load_from_dump(file_obj):
	from struct import Struct
	header = Struct('IQ?IH')
	while True:
		data = file_obj.read(header.size)
		if not data:
			return
		yield RawPacket(
			*header.unpack(data),
			GameNetwork.get_dynamic_length_data(file_obj),
			GameNetwork.get_dynamic_length_data(file_obj)
		)
