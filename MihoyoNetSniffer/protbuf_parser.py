import os.path
import sys
from importlib.util import spec_from_file_location, module_from_spec
from concurrent.futures import ThreadPoolExecutor
from .packet import RawPacket

parser_code_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'generated_python_code'
sys.path.insert(0, parser_code_path)


def module_import_helper(cmd_name):
	if cmd_name + '_pb2' in sys.modules:
		module = sys.modules[cmd_name + '_pb2']
	else:
		package_name = cmd_name + '_pb2.py'
		spec = spec_from_file_location(name=package_name, location=parser_code_path + os.sep + package_name)
		module = module_from_spec(spec)
		spec.loader.exec_module(module)
	return module.__dict__[cmd_name]


def load_parsers(file):
	def load_core(name, packet_id):
		cmd_id_map[packet_id] = module_import_helper(name)
		cmd_name_map[name] = packet_id

	thread_pool = ThreadPoolExecutor()
	cmd_id_map = {}
	cmd_name_map = {}
	tasks = []
	for line in file.readlines():
		cmd_name, cmd_id = line.split(',')
		cmd_id = int(cmd_id[:-1])
		tasks.append(thread_pool.submit(load_core, cmd_name, cmd_id))
	head_load = thread_pool.submit(module_import_helper, 'PacketHead')
	for task in tasks:
		task.result()
	head_load = head_load.result()
	thread_pool.shutdown()
	return cmd_id_map, cmd_name_map, head_load


class ProtobufParser:
	def __init__(self, cmdid_path):
		with open(cmdid_path, 'r') as f:
			self.cmd_id_map, self.cmd_name_map, self.packet_header = load_parsers(f)

	def parse_raw_packet(self, raw_packet: RawPacket):
		header = self.packet_header()
		packet = self.cmd_id_map[raw_packet.message_id]()
		header.ParseFromString(raw_packet.header)
		packet.ParseFromString(raw_packet.content)
		return header, packet

	def get_packet_name(self, packet_id: int):
		return self.cmd_id_map[packet_id].DESCRIPTOR.name

	def __getitem__(self, item: int or str):
		if isinstance(item, int):
			return self.cmd_id_map[item]
		if isinstance(item, str):
			return self.cmd_id_map[self.cmd_name_map[item]]
