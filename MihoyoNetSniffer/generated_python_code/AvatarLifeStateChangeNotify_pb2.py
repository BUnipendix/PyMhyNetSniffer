# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AvatarLifeStateChangeNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import PlayerDieType_pb2 as PlayerDieType__pb2
import ServerBuff_pb2 as ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!AvatarLifeStateChangeNotify.proto\x1a\x13PlayerDieType.proto\x1a\x10ServerBuff.proto\"\xd8\x01\n\x1b\x41vatarLifeStateChangeNotify\x12\x18\n\x10source_entity_id\x18\x0b \x01(\r\x12%\n\x10server_buff_list\x18\x0e \x03(\x0b\x32\x0b.ServerBuff\x12\x19\n\x11move_reliable_seq\x18\x0c \x01(\r\x12\x12\n\nlife_state\x18\x06 \x01(\r\x12 \n\x08\x64ie_type\x18\x05 \x01(\x0e\x32\x0e.PlayerDieType\x12\x12\n\nattack_tag\x18\x0f \x01(\t\x12\x13\n\x0b\x61vatar_guid\x18\x02 \x01(\x04\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AvatarLifeStateChangeNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AVATARLIFESTATECHANGENOTIFY._serialized_start=77
  _AVATARLIFESTATECHANGENOTIFY._serialized_end=293
# @@protoc_insertion_point(module_scope)
