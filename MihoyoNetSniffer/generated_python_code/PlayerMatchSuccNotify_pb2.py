# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerMatchSuccNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GeneralMatchInfo_pb2 as GeneralMatchInfo__pb2
import MatchType_pb2 as MatchType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bPlayerMatchSuccNotify.proto\x1a\x16GeneralMatchInfo.proto\x1a\x0fMatchType.proto\"\xde\x01\n\x15PlayerMatchSuccNotify\x12\"\n\x1amechanicus_difficult_level\x18\x01 \x01(\r\x12\x12\n\ndungeon_id\x18\x06 \x01(\r\x12\x1e\n\nmatch_type\x18\x05 \x01(\x0e\x32\n.MatchType\x12\x12\n\nmp_play_id\x18\x0f \x01(\r\x12-\n\x12general_match_info\x18\x07 \x01(\x0b\x32\x11.GeneralMatchInfo\x12\x10\n\x08host_uid\x18\x03 \x01(\r\x12\x18\n\x10\x63onfirm_end_time\x18\x02 \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerMatchSuccNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERMATCHSUCCNOTIFY._serialized_start=73
  _PLAYERMATCHSUCCNOTIFY._serialized_end=295
# @@protoc_insertion_point(module_scope)
