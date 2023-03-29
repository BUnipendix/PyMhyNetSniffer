import sys
from dataclasses import dataclass
from enum import IntEnum
from google.protobuf.message import Message
from struct import Struct
from dataclasses import dataclass, is_dataclass


class ModifyType(IntEnum):
	Unchanged = 0
	Blocked = 1
	Modified = 2


class PacketType(IntEnum):
	Null = 0
	PacketData = 1
	ModifyData = 2


class Direction(IntEnum):
	Send = 0
	Receive = 1


@dataclass(repr=False, eq=False)
class PipeHeader:
	packet_type: PacketType = PacketType.Null
	time_stamp: int = 0


@dataclass(repr=False, eq=False)
class RawPacketInfo:
	manipulation_enabled: bool = False
	direction: Direction = Direction.Send
	message_id: int = 0


@dataclass(repr=False, eq=False)
class ModifyPacketInfo:
	modify_type: ModifyType = ModifyType.Unchanged
	message_id: int = 0


@dataclass(repr=False, eq=False)
class RawPacket:
	time_stamp: int = 0
	direction: Direction = Direction.Send
	message_id: int = 0
	header: Message = b''
	content: Message = b''


class MessageList(list):
	def __str__(self):
		cmd_str = "\n".join((i.DESCRIPTOR.name + ':\n' + str(i) for i in self))
		return f'cmd_list [\n{cmd_str}]'


class DataclassIO:
	def __init__(self, data_class, struct_code, read_func = None, write_func = None):
		self._struct = Struct(struct_code)
		if callable(read_func):
			self._read = read_func
		if callable(write_func) is False:
			self._write = write_func
		self._data_class = data_class
		# TODO 自动转换Enum
		# for i in data_class.

	def read(self):
		return self._data_class(*self._struct.unpack(self._read(self._struct.size)))

	def write(self, data):
		self._write(self._struct.pack(data.__dict__.values()))

