from logging import getLogger
logger = getLogger('MihoyoNetSniffer.Util')
COMMON_UNIMPORTENT_PACKETS = (
	'PlayerGameTimeNotify',
	'PlayerTimeNotify',
	'WorldPlayerRTTNotify',
	'PlayerSetPauseRsp',
	'PlayerSetPauseReq',
	'PingReq',
	'PingRsp',
)


def get_main_dir():
	from os.path import dirname, abspath
	return dirname(abspath(__file__))


def check_filename(filename):
	import os
	new_filename, suffix = os.path.splitext(filename)
	count = 1
	while os.path.exists(new_filename + suffix):
		new_filename = f'{filename}({count})'
		count += 1
	return new_filename + suffix


def generate_printed_packet(packet):
	from .sniffer import MessageList
	from google.protobuf.message import Message
	from google.protobuf.text_format import MessageToString
	from time import localtime, strftime
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
	return f'\n{format_time}  有消息:{packet_name}\n{print_data}\n'