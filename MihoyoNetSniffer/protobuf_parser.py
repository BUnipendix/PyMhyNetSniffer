from .data_type import UnknownPacket
from .constant import PROTO_NAME
from .util import main_dir
from logging import getLogger
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


class ProtobufParser:
	def __init__(self, proto_path=main_dir, proto_name=PROTO_NAME):
		print(__name__)
		print(__file__)
		from pathlib import Path
		from importlib.util import spec_from_file_location, module_from_spec

		proto_path = Path(proto_path)
		cmdid_path = proto_path / 'cmdid.csv'
		bp_path = proto_path / (proto_name + '_pb2.py')
		self._cmd_id_map = {}
		self._cmd_name_map = {}

		# import parsers
		spec = spec_from_file_location(proto_name, bp_path.__str__())
		if spec is None:
			raise ImportError(f'找不到proto：{bp_path.__str__()}')
		module = module_from_spec(spec)
		spec.loader.exec_module(module)

		raw_field_dict = module.__dict__
		for line in cmdid_path.open(encoding='utf-8'):
			cmd_name, cmd_id = line.split(',')
			cmd_id = int(cmd_id[:-1])
			self._cmd_name_map[cmd_name.lower()] = cmd_id
			cmd_parser = raw_field_dict.get(cmd_name, None)
			if cmd_parser is None:
				logger.error('找不到protobuf解析器模块：' + cmd_name)
			self._cmd_id_map[cmd_id] = cmd_parser
		self.packet_header_parser = raw_field_dict.get('PacketHead', None)

	def parse_packet(self, message_id: int, content: bytes):
		parser = self.get_packet_parser(message_id)
		if parser is None:
			packet = UnknownPacket(message_id, content)
		else:
			packet = self.parse_core(content, parser)
		return packet

	def parse_header(self, header: bytes):
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
