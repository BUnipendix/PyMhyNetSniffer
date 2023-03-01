from dataclasses import dataclass
from time import localtime, strftime
from google.protobuf.message import Message
from google.protobuf.text_format import MessageToString
from MihoyoNetSniffer.packet import GameNetwork, Thread, Direction
from MihoyoNetSniffer.protbuf_parser import ProtobufParser


@dataclass
class ParsedPacket:
	time_stamp: int
	direction: Direction
	header: Message
	content: Message


class Sniffer:
	def __init__(self, pipe_name='genshin_packet_pipe', dump_file: str = None, cache_packet=True, enable_data_output=False):
		"""
		:param pipe_name: Cheat output pipe name
		:param dump_file: Dump file path
		:param cache_packet: Enable cache packet in class
		:param enable_data_output: Enable save readable data
		"""
		from os import sep, getcwd
		self.cache_packet_flag = cache_packet
		root = getcwd() + sep + 'MihoyoNetSniffer' + sep
		cmdid_path = root + 'cmdid.csv'
		if enable_data_output:
			self._f_output = open('parsed_data.txt', 'w', encoding='utf-8')
		else:
			self._f_output = None
		self.socket_client = GameNetwork(pipe_name, dump_file)
		self.protobuf_parser = ProtobufParser(cmdid_path)
		self.handle = {}
		self.packet_time_index = {}
		self.process_loop = Thread(target=self._packet_process_loop)
		self.packets = []

	def log(self, info):
		if self._f_output:
			print(info, file=self._f_output)
			self._f_output.flush()

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
		if self._f_output:
			self._f_output.close()

	def load_from_file(self, file_path):
		"""
		Load dump data from file and saved in file
		"""
		def yield_wrapper():
			return next(iter_obj, None)

		from MihoyoNetSniffer.packet import load_from_dump
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
			packet_time = raw_packet.time_stamp
			time_int, time_float = divmod(packet_time, 1000)
			self.log(f'\n{strftime("%Y-%m-%d %H:%M:%S" ,localtime(time_int))}.{time_float}  有消息:{self.protobuf_parser.get_packet_name(raw_packet.message_id)}')
			packet = ParsedPacket(
				raw_packet.time_stamp, raw_packet.direction,
				*self.protobuf_parser.parse_raw_packet(raw_packet)
			)
			if isinstance(packet.content, Message):
				print_data = MessageToString(packet.content, as_utf8=True, use_short_repeated_primitives=True)
			else:
				print_data = packet.content
			self.log(print_data)
			if self.cache_packet_flag:
				self.packet_time_index[packet_time] = len(self.packets)
				self.packets.append(packet)
			handles = self.handle.get(raw_packet.message_id, None)
			del raw_packet
			if not handles:
				continue
			for handle in handles:
				handle(packet_time, packet)  # 到底要不要多线程呢
