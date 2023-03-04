from logging import getLogger
from .data_type import Direction
from google.protobuf.json_format import ParseDict, MessageToDict
from .data_type import MessageList, ParsedPacket
from google.protobuf.message import Message
from google.protobuf.text_format import MessageToString
from time import localtime, strftime
logger = getLogger('MihoyoNetSniffer.Util')
from os.path import dirname, abspath
main_dir = dirname(abspath(__file__))


def check_filename(filename):
	import os
	new_filename, suffix = os.path.splitext(filename)
	count = 1
	while os.path.exists(new_filename + suffix):
		new_filename = f'{filename}({count})'
		count += 1
	return new_filename + suffix


def json2pb(data, parser):
	message = parser()
	return ParseDict(data, message)


def pb2json(message):
	return MessageToDict(message)


def get_direction_name(direction: Direction):
	return '接收' if direction == Direction.Receive else '发出'


def generate_printed_packet_name(packet: Message):
	if isinstance(packet, Message):
		return packet.DESCRIPTOR.name
	elif isinstance(packet, MessageList):
		return f'[{",".join(generate_printed_packet_name(i) for i in packet)}]'
	else:
		return packet


def generate_printed_packet(packet: ParsedPacket):
	time_int, time_float = divmod(packet.time_stamp, 1000)
	format_time = f'{strftime("%Y-%m-%d %H:%M:%S", localtime(time_int))}.{time_float}'
	if isinstance(packet.content, Message):
		print_data = MessageToString(packet.content, as_utf8=True, use_short_repeated_primitives=True)
		packet_name = packet.content.__class__.__name__
	elif isinstance(packet.content, MessageList):
		print_data = ''.join(f'子消息：{i.DESCRIPTOR.name}\n' + MessageToString(i, as_utf8=True, use_short_repeated_primitives=True) for i in packet.content)
		return f'\n{format_time} 有消息集：\n{print_data}\n'
	else:
		packet_name, print_data = packet.content
		logger.debug(f'检测到未解析的包：{packet_name}，内容：{print_data}')
	return f'\n{format_time}	有{get_direction_name(packet.direction)}的消息:{packet_name}\n{print_data}\n'