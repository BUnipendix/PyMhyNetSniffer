import os
from dataclasses import dataclass
from time import localtime, strftime
from logging import getLogger
from traceback import format_exc
from sortedcontainers.sorteddict import SortedDict
from collections import defaultdict
from google.protobuf.message import Message
from google.protobuf.text_format import MessageToString
from .packet import GameNetwork, Thread, Direction
from .protbuf_parser import ProtobufParser, UnknownPacket
from .util import check_filename
logger = getLogger('MihoyoNetSniffer.Sniffer')

@dataclass
class ParsedPacket:
	time_stamp: int
	direction: Direction
	header: Message
	content: Message or UnknownPacket


class Sniffer:
	def __init__(
			self,
			pipe_name='genshin_packet_pipe',
			dump_path: str = None,
			white_list_mode=False,
			cache_packet=True,
			enable_data_output=False):
		"""
		:param pipe_name: Cheat output pipe name
		:param dump_path: Dump file path
		:param white_list_mode: not enable is blacklist mode
		use add_to_list/remove_from_list to change the blacklist/whitelist
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
			self._data_output = open(check_filename('parsed_data.txt'), 'w', encoding='utf-8')
		else:
			self._data_output = None
		if dump_path:
			dump_filename = dump_path + os.sep + strftime("GenshinKCP-%Y-%m-%d-%H-%M-%S.dump", localtime())
		else:
			dump_filename = None
		self.socket_client = GameNetwork(pipe_name, dump_filename)
		self.wait_for_connected = self.socket_client.wait_for_connected
		self.protobuf_parser = ProtobufParser(cmdid_path)
		self.handles = defaultdict(list)
		self._process_loop = Thread(target=self._packet_process_loop)
		self.packets = SortedDict()
		self.white_list_mode = white_list_mode
		self._filter_list = set()  # black or white list

	def _data_log(self, info):
		if self._data_output:
			print(info, file=self._data_output)
			self._data_output.flush()

	def add_to_list(self, *packet_name):
		"""
		add packet type to filter list
		:param packet_name: packets' name
		"""
		for i in packet_name:
			cmd_id = self.protobuf_parser[i]
			if cmd_id is not None:
				self._filter_list.add(cmd_id)

	def remove_from_list(self, *packet_name):
		"""
		remove packet type from filter list
		:param packet_name: packets' name
		"""
		for i in packet_name:
			cmd_id = self.protobuf_parser[i]
			if cmd_id is not None:
				self._filter_list.discard(cmd_id)

	def add_handle(self, packet_name, func):
		logger.info(f'添加{func.__name__}为{packet_name}包的回调处理函数')
		packet_id = self.protobuf_parser[packet_name]
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

	def _add_packet(self, packet: ParsedPacket):
		logger.debug(f'添加包{packet.content.__class__.__name__}')
		self.packets[packet.time_stamp] = packet

	def add_packet(self, packet: ParsedPacket):
		message_id = self.protobuf_parser[packet.__class__.__name__]
		if (message_id in self._filter_list) ^ self.white_list_mode:
			self._add_packet(packet)

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
				self._add_packet(packet)

	@staticmethod
	def generate_printed_packet(packet: ParsedPacket):
		time_int, time_float = divmod(packet.time_stamp, 1000)
		if isinstance(packet.content, Message):
			print_data = MessageToString(packet.content, as_utf8=True, use_short_repeated_primitives=True)
			packet_name = packet.content.__class__.__name__
		else:
			packet_name, print_data = packet.content
			logger.debug(f'检测到未录入的包：{packet_name}，内容：{print_data}')
		return f'\n{strftime("%Y-%m-%d %H:%M:%S", localtime(time_int))}.{time_float}  有消息:{packet_name}\n{print_data}'

	def _packet_process_loop(self, override_func=None):
		# prepare
		if override_func:
			get_packet = override_func
			logger.debug('循环：覆盖原有获取原始函数:' + override_func.__name__)
			logger.debug(format_exc())
		else:
			get_packet = self.socket_client.get_packet

		while True:
			# parse raw packet
			raw_packet = get_packet()
			if raw_packet is None:
				return
			message_id = raw_packet.message_id

			if (message_id in self._filter_list) ^ self.white_list_mode:
				continue

			packet = ParsedPacket(
				raw_packet.time_stamp, raw_packet.direction,
				*self.protobuf_parser.parse_raw_packet(raw_packet)
			)
			del raw_packet

			# process packet
			if self._data_output:
				self._data_log(self.generate_printed_packet(packet))
			if self.cache_packet_flag:
				self._add_packet(packet)
			if isinstance(packet.content, Message):
				handles = self.handles.get(message_id, None)
				if not handles:
					continue
				for handle in handles:
					handle(packet.time_stamp, packet)  # 到底要不要多线程呢

	def __del__(self):
		self.socket_client.__del__()
		del self.socket_client, self.wait_for_connected
		if self._process_loop.is_alive():
			self._process_loop.join()
		if self._data_output:
			self._data_output.close()

