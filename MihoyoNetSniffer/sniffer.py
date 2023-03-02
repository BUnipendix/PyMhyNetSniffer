from dataclasses import dataclass
from time import localtime, strftime
from logging import getLogger
from traceback import format_exc
from sortedcontainers.sorteddict import SortedDict
from collections import defaultdict
from google.protobuf.message import Message
from google.protobuf.text_format import MessageToString
from .packet import GameNetwork, Thread, Direction
from .protbuf_parser import ProtobufParser
logger = getLogger('Sniffer')

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
		from .util import get_main_dir
		from os import sep
		self.cache_packet_flag = cache_packet
		root = get_main_dir() + sep
		cmdid_path = root + 'cmdid.csv'
		if enable_data_output:
			logger.info('Enable parsed data output')
			self._f_output = open('parsed_data.txt', 'w', encoding='utf-8')
		else:
			self._f_output = None
		self.socket_client = GameNetwork(pipe_name, dump_file)
		self.wait_for_connected = self.socket_client.wait_for_connected
		self.protobuf_parser = ProtobufParser(cmdid_path)
		self.handles = defaultdict(list)
		self._process_loop = Thread(target=self._packet_process_loop)
		self.packets = SortedDict()

	def _data_log(self, info):
		if self._f_output:
			print(info, file=self._f_output)
			self._f_output.flush()

	def add_handle(self, packet_name, func):
		logger.info(f'hook添加{func.__name__}为{packet_name}包的回调处理函数')
		packet_id = self.protobuf_parser.cmd_name_map[packet_name]
		self.handles[packet_id].append(func)

	def start(self):
		logger.debug('启动抓包器')
		self.socket_client.start()
		if self._process_loop.is_alive() is False:
			self._process_loop.start()

	def stop(self):
		logger.debug('关闭抓包器')
		self.socket_client.stop()
		if self._process_loop.is_alive():
			self._process_loop.join()
		logger.debug('关闭成功')

	def look_for_packets_in_range_time(self, min_time: int, max_time: int, inclusive=(True,True)):
		for time in self.packets.irange(min_time, max_time, inclusive):
			yield time, self.packets[time]

	def add_packet(self, packet: ParsedPacket):
		logger.debug(f'添加包{packet.content.__name__}')
		self.packets[packet.time_stamp] = packet

	def load_from_file(self, file_path):
		"""
		Load dump data from file and saved in file
		"""
		from .packet import load_from_dump
		with open(file_path, 'rb') as f:
			for raw_packet in load_from_dump(f):
				packet = ParsedPacket(
					raw_packet.time_stamp, raw_packet.direction,
					*self.protobuf_parser.parse_raw_packet(raw_packet)
				)
				self.add_packet(packet)

	def _packet_process_loop(self, override_func=None):
		if override_func:
			get_packet = override_func
			logger.debug('循环：覆盖原有获取原始函数:' + override_func.__name__)
			logger.debug(format_exc())
		else:
			get_packet = self.socket_client.get_packet
		while True:
			raw_packet = get_packet()
			if raw_packet is None:
				return
			message_id = raw_packet.message_id
			packet = ParsedPacket(
				raw_packet.time_stamp, raw_packet.direction,
				*self.protobuf_parser.parse_raw_packet(raw_packet)
			)
			del raw_packet
			# print packet info
			if self._f_output:
				time_int, time_float = divmod(packet.time_stamp, 1000)
				self._data_log(f'\n{strftime("%Y-%m-%d %H:%M:%S", localtime(time_int))}.{time_float}  有消息:{self.protobuf_parser.get_packet_name(message_id)}')
				if isinstance(packet.content, Message):
					print_data = MessageToString(packet.content, as_utf8=True, use_short_repeated_primitives=True)
				else:
					print_data = packet.content
					logger.debug(f'检测到未录入的包：{message_id}，内容：{print_data}')
				self._data_log(print_data)
			if self.cache_packet_flag:
				self.add_packet(packet)
			handles = self.handles.get(message_id, None)
			if not handles:
				continue
			for handle in handles:
				handle(packet.time_stamp, packet)  # 到底要不要多线程呢

	def __del__(self):
		logger.debug('回收实例')
		self.stop()
		if self._f_output:
			self._f_output.close()

