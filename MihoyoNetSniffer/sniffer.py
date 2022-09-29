from dataclasses import dataclass
from os import PathLike

from google.protobuf.message import Message

from .packet import GameNetwork, Thread, Direction
from .protbuf_parser import ProtobufParser


@dataclass
class ParsedPacket:
	time_stamp: int
	direction: Direction
	header: Message
	content: Message


class Sniffer:
	def __init__(self, cmdid_path, pipe_name='genshin_packet_pipe', dump_file: str = None):
		self.socket_client = GameNetwork(pipe_name, dump_file)
		self.protobuf_parser = ProtobufParser(cmdid_path)
		self.handle = {}
		self.process_loop = Thread(target=self._packet_process_loop)
		self.packets = []

	def add_handle(self, packet_name, func):
		packet_id = self.protobuf_parser.cmd_name_map[packet_name]
		old_handles = self.handle.get(packet_id, None)
		if old_handles:
			old_handles.append(func)
			return
		self.handle[packet_id] = [func]

	def start(self):
		self.socket_client.start()
		self.process_loop.start()

	def stop(self):
		self.socket_client.stop()
		self.process_loop.join()

	def load_from_file(self, file_path):
		def yield_wrapper():
			return next(iter_obj, None)

		from .packet import load_from_dump
		with open(file_path, 'rb') as f:
			iter_obj = load_from_dump(f)
			self._packet_process_loop(load_from_dump(yield_wrapper))

	def _packet_process_loop(self, override_func=None):
		if override_func:
			get_packet = override_func
		else:
			get_packet = self.socket_client.get_packet
		while True:
			raw_packet = get_packet()
			if raw_packet is None:
				return
			# print(f'有消息:{self.protobuf_parser.get_packet_name(raw_packet.message_id)}')
			packet = ParsedPacket(
				raw_packet.time_stamp, raw_packet.direction,
				*self.protobuf_parser.parse_raw_packet(raw_packet)
			)
			count = len(self.packets)
			self.packets.append(packet)
			handles = self.handle.get(raw_packet.message_id, None)
			del raw_packet
			if not handles:
				continue
			for handle in handles:
				handle(count, packet)  # 到底要不要多线程呢
