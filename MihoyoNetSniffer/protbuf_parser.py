import os.path
import sys
from importlib.util import spec_from_file_location, module_from_spec
from .packet import RawPacket
from dataclasses import dataclass

"""parser_code_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'generated_python_code'
sys.path.insert(0, parser_code_path)"""


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


def load_parsers(file):
	from importlib import import_module
	cmd_id_map = {}
	cmd_name_map = {}
	raw_field_dict = import_module('.genshin_proto_pb2', __package__).__dict__
	for line in file.readlines():
		cmd_name, cmd_id = line.split(',')
		cmd_id = int(cmd_id[:-1])
		cmd_name_map[cmd_name] = cmd_id
		cmd_id_map[cmd_id] = raw_field_dict.get(cmd_name, None)
	head_load = raw_field_dict.get('PacketHead', None)
	return cmd_id_map, cmd_name_map, head_load


class ProtobufParser:
	def __init__(self, cmdid_path):
		with open(cmdid_path, 'r') as f:
			self.cmd_id_map, self.cmd_name_map, self.packet_header = load_parsers(f)

	def parse_raw_packet(self, raw_packet: RawPacket):
		header = self._parse_core(raw_packet.header, self.packet_header)
		packet = self._parse_core(raw_packet.content, self.cmd_id_map[raw_packet.message_id])
		return header, packet

	def get_packet_name(self, packet_id: int):
		return self.cmd_id_map[packet_id].DESCRIPTOR.name

	@staticmethod
	def _parse_core(raw_data: bytes, parser):
		if parser is None:
			return raw_data
		parser = parser()
		parser.ParseFromString(raw_data)
		return parser

	def __getitem__(self, item: int or str):
		if isinstance(item, int):
			return self.cmd_id_map[item]
		if isinstance(item, str):
			return self.cmd_id_map[self.cmd_name_map[item]]
