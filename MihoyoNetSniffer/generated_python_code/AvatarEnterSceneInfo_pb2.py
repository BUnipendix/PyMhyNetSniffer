# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AvatarEnterSceneInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import AbilitySyncStateInfo_pb2 as AbilitySyncStateInfo__pb2
import ServerBuff_pb2 as ServerBuff__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x41vatarEnterSceneInfo.proto\x1a\x1a\x41\x62ilitySyncStateInfo.proto\x1a\x10ServerBuff.proto\"\x99\x02\n\x14\x41vatarEnterSceneInfo\x12%\n\x10server_buff_list\x18\x0e \x03(\x0b\x32\x0b.ServerBuff\x12\x18\n\x10\x61vatar_entity_id\x18\x07 \x01(\r\x12\x32\n\x13weapon_ability_info\x18\x0c \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x18\n\x10weapon_entity_id\x18\n \x01(\r\x12\x32\n\x13\x61vatar_ability_info\x18\x02 \x01(\x0b\x32\x15.AbilitySyncStateInfo\x12\x13\n\x0b\x61vatar_guid\x18\r \x01(\x04\x12\x13\n\x0bweapon_guid\x18\t \x01(\x04\x12\x14\n\x0c\x62uff_id_list\x18\x05 \x03(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'AvatarEnterSceneInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _AVATARENTERSCENEINFO._serialized_start=77
  _AVATARENTERSCENEINFO._serialized_end=358
# @@protoc_insertion_point(module_scope)