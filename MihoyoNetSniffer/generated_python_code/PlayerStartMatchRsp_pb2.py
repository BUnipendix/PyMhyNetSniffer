# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerStartMatchRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MatchType_pb2 as MatchType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19PlayerStartMatchRsp.proto\x1a\x0fMatchType.proto\"\xcc\x01\n\x13PlayerStartMatchRsp\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x12\x17\n\x0fpunish_end_time\x18\x05 \x01(\r\x12\r\n\x05param\x18\x04 \x01(\r\x12\x12\n\nmp_play_id\x18\r \x01(\r\x12\"\n\x1amechanicus_difficult_level\x18\x02 \x01(\r\x12\x12\n\ndungeon_id\x18\x03 \x01(\r\x12\x10\n\x08match_id\x18\x08 \x01(\r\x12\x1e\n\nmatch_type\x18\x07 \x01(\x0e\x32\n.MatchTypeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerStartMatchRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERSTARTMATCHRSP._serialized_start=47
  _PLAYERSTARTMATCHRSP._serialized_end=251
# @@protoc_insertion_point(module_scope)
