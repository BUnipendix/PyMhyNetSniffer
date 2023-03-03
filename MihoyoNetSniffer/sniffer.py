from pathlib import Path
from dataclasses import dataclass
from time import localtime, strftime
from logging import getLogger
from traceback import format_exc
from sortedcontainers.sorteddict import SortedDict
from collections import defaultdict
from google.protobuf.message import Message
from .packet import PipePacketStream, Thread, Direction, RawPacket
from .protbuf_parser import ProtobufParser, UnknownPacket
from .util import check_filename
logger = getLogger('MihoyoNetSniffer.Sniffer')


@dataclass
class ParsedPacket:
	time_stamp: int
	direction: Direction
	header: Message
	content: Message or UnknownPacket


class MessageList(list):
	def __str__(self):
		cmd_str = "\n".join((i.DESCRIPTOR.name + ':\n' + str(i) for i in self))
		return f'cmd_list [\n{cmd_str}]'


class Sniffer:
	def __init__(
			self,
			pipe_name='genshin_packet_pipe',
			dump_path: str = None,
			whitelist_mode=False,
			cache_packet=True,
			enable_data_output=False):
		"""
		:param pipe_name: Cheat output pipe name
		:param dump_path: Dump file path
		:param whitelist_mode: not enable is blacklist mode
		use add_to_list/remove_from_list to change the blacklist/whitelist
		:param cache_packet: Enable cache packet in class
		:param enable_data_output: Enable save readable data
		"""
		from .util import get_main_dir
		self.cache_packet_flag = cache_packet
		self._whitelist_mode = whitelist_mode
		self._process_loop = Thread(target=self._packet_process_loop)
		root = Path(get_main_dir())
		cmdid_path = root / 'cmdid.csv'

		if enable_data_output:
			logger.info('Enable parsed data output')
			self._data_output = open(check_filename('parsed_data.txt'), 'w', encoding='utf-8')
		else:
			self._data_output = None

		if dump_path:
			dump_path = Path(dump_path)
			dump_filename = dump_path / strftime("GenshinKCP-%Y-%m-%d-%H-%M-%S.dump", localtime())
		else:
			dump_filename = None

		self.socket_client = PipePacketStream(pipe_name, dump_filename)
		self.wait_for_connected = self.socket_client.wait_for_connected
		self.protobuf_parser = ProtobufParser(cmdid_path)
		self._union_cmd_notify_id = self.protobuf_parser['UnionCmdNotify']

		self.handles = defaultdict(list)
		self.packets = SortedDict()
		self._filter_list = set()  # black or white list

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

	def look_for_packets_in_range_time(self, min_time: int, max_time: int, inclusive=(True,True)):
		for time in self.packets.irange(min_time, max_time, inclusive):
			yield time, self.packets[time]

	def load_from_file(self, file_path, call_handle=False):
		"""
		Load dump data from file and saved in file
		"""
		from .packet import load_from_dump
		with open(file_path, 'rb') as f:
			for raw_packet in load_from_dump(f):
				packet = self.parse_raw_packet(raw_packet, call_handle)
				if packet:
					self._add_packet(packet)

	def parse_raw_packet(self, raw_packet: RawPacket, call_handle):
		message = self._message_global_process(
			raw_packet.message_id, raw_packet.content,
			call_handle, raw_packet.time_stamp
		)
		if not message:
			return
		header = self.protobuf_parser.parse_header(raw_packet.header)
		return ParsedPacket(
			raw_packet.time_stamp, raw_packet.direction,
			header, message
		)

	def _add_packet(self, packet: ParsedPacket):
		self.packets[packet.time_stamp] = packet

	def _message_global_process(
			self,
			message_id: int,
			body: bytes or bytearray,
			need_handle_callback,
			time_stamp=0):
		"""使用了递归不断解析UnionCmdNotify"""
		message = self.protobuf_parser.parse_packet(message_id, body)

		if message_id == self._union_cmd_notify_id:
			# 处理messageList
			new_list = []
			for i in message.cmd_list:
				# 套娃
				sub_message = self._message_global_process(i.message_id, i.body, need_handle_callback, time_stamp)
				if sub_message:
					new_list.append(sub_message)
			return MessageList(new_list)

		else:
			# 处理普通message
			if (message_id not in self._filter_list) ^ self._whitelist_mode:
				if need_handle_callback and isinstance(message, bytes) is False:
					handles = self.handles.get(message_id, None)
					if handles:
						for handle in handles:
							ret = handle(time_stamp, message)  # 到底要不要多线程呢
							if ret:
								message = ret
				return message

	def _packet_process_loop(self, override_func=None):
		from .util import generate_printed_packet
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

			packet = self.parse_raw_packet(raw_packet, True)
			if packet is None:
				continue

			# process packet
			if self._data_output:
				self._data_log(generate_printed_packet(packet))
			if self.cache_packet_flag:
				self._add_packet(packet)

	def _data_log(self, info):
		if self._data_output:
			print(info, file=self._data_output)
			self._data_output.flush()

	def __del__(self):
		self.socket_client.__del__()
		del self.socket_client, self.wait_for_connected
		if self._process_loop.is_alive():
			self._process_loop.join()
		if self._data_output:
			self._data_output.close()
