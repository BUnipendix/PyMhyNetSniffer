# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OtherCustomDungeonBrief.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CustomDungeonAbstract_pb2 as CustomDungeonAbstract__pb2
import CustomDungeonSetting_pb2 as CustomDungeonSetting__pb2
import CustomDungeonSocial_pb2 as CustomDungeonSocial__pb2
import SocialDetail_pb2 as SocialDetail__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dOtherCustomDungeonBrief.proto\x1a\x1b\x43ustomDungeonAbstract.proto\x1a\x1a\x43ustomDungeonSetting.proto\x1a\x19\x43ustomDungeonSocial.proto\x1a\x12SocialDetail.proto\"\xdc\x02\n\x17OtherCustomDungeonBrief\x12\x1c\n\x14is_adventure_dungeon\x18\x0c \x01(\x08\x12\x1c\n\x14\x62\x61ttle_min_cost_time\x18\n \x01(\r\x12\x10\n\x08tag_list\x18\r \x03(\r\x12\x11\n\tis_stored\x18\x08 \x01(\x08\x12\x12\n\ndungeon_id\x18\x0f \x01(\r\x12\x17\n\x0fis_psn_platform\x18\x01 \x01(\x08\x12\x14\n\x0c\x64ungeon_guid\x18\x07 \x01(\x04\x12&\n\x07setting\x18\x02 \x01(\x0b\x32\x15.CustomDungeonSetting\x12$\n\x06social\x18\x0e \x01(\x0b\x32\x14.CustomDungeonSocial\x12(\n\x08\x61\x62stract\x18\x04 \x01(\x0b\x32\x16.CustomDungeonAbstract\x12%\n\x0e\x63reator_detail\x18\x0b \x01(\x0b\x32\r.SocialDetailb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'OtherCustomDungeonBrief_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _OTHERCUSTOMDUNGEONBRIEF._serialized_start=138
  _OTHERCUSTOMDUNGEONBRIEF._serialized_end=486
# @@protoc_insertion_point(module_scope)
