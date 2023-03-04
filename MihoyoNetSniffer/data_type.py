from dataclasses import dataclass
from enum import IntEnum
from google.protobuf.message import Message


class PacketType(IntEnum):
	Null = 0
	PacketData = 1
	ModifyData = 2


class Direction(IntEnum):
	Send = 0
	Receive = 1


@dataclass
class RawPacket:
	packet_type: PacketType
	time_stamp: int
	manipulation_enabled: bool
	direction: Direction
	message_id: int
	header: bytes = b''
	content: bytes = b''


@dataclass
class UnknownPacket:
	message_id: int
	content: bytes


class MessageList(list):
	def __str__(self):
		cmd_str = "\n".join((i.DESCRIPTOR.name + ':\n' + str(i) for i in self))
		return f'cmd_list [\n{cmd_str}]'


@dataclass
class ParsedPacket:
	time_stamp: int
	direction: Direction
	header: Message
	content: Message or UnknownPacket or MessageList
