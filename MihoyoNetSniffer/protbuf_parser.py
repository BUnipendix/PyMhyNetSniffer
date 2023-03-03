from .packet import RawPacket
from logging import getLogger
from dataclasses import dataclass
from google.protobuf import json_format
logger = getLogger('MihoyoNetSniffer.ProtobufParser')
"""def module_import_helper(cmd_name):
	from .util import get_main_dir
	if cmd_name + '_pb2' in sys.modules:
		module = sys.modules[cmd_name + '_pb2']
	else:
		package_name = cmd_name + '_pb2.py'
		spec = spec_from_file_location(name=package_name, location=get_main_dir() + os.sep + package_name)
		module = module_from_spec(spec)
		spec.loader.exec_module(module)
	return module.__dict__"""


@dataclass
class UnknownPacket:
	message_id: int
	content: bytes


def load_parsers(file):
	from importlib import import_module
	cmd_id_map = {}
	cmd_name_map = {}
	raw_field_dict = import_module('.genshin_proto_pb2', __package__).__dict__
	for line in file.readlines():
		cmd_name, cmd_id = line.split(',')
		cmd_id = int(cmd_id[:-1])
		cmd_name_map[cmd_name.lower()] = cmd_id
		cmd_parser = raw_field_dict.get(cmd_name, None)
		if cmd_parser is None:
			logger.error('找不到protobuf解析器模块：' + cmd_name)
		cmd_id_map[cmd_id] = cmd_parser
	head_load = raw_field_dict.get('PacketHead', None)
	return cmd_id_map, cmd_name_map, head_load


class ProtobufParser:
	def __init__(self, cmdid_path):
		with open(cmdid_path, 'r') as f:
			self._cmd_id_map, self._cmd_name_map, self.packet_header_parser = load_parsers(f)

	def parse_packet(self, message_id, content):
		parser = self.get_packet_parser(message_id)
		if parser is None:
			packet = UnknownPacket(message_id, content)
		else:
			packet = self.parse_core(content, parser)
		return packet

	def parse_header(self, header):
		return self.parse_core(header, self.packet_header_parser)

	def get_packet_parser(self, packet_id: int):
		return self._cmd_id_map.get(packet_id, None)

	@staticmethod
	def parse_core(raw_data: bytes, parser):
		if parser is None:
			return raw_data
		parser = parser()
		parser.ParseFromString(raw_data)
		return parser

	def __getitem__(self, item: int or str):
		try:
			if isinstance(item, int):
				return self._cmd_id_map[item].DESCRIPTOR.name
			if isinstance(item, str):
				return self._cmd_name_map[item.lower()]
		except KeyError:
			return None


def json2pb(data, parser):
	message = parser()
	return json_format.ParseDict(data, message)


def pb2json(message):
	return json_format.MessageToDict(message)
