# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BattlePassAllDataNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BattlePassMission_pb2 as BattlePassMission__pb2
import BattlePassSchedule_pb2 as BattlePassSchedule__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x42\x61ttlePassAllDataNotify.proto\x1a\x17\x42\x61ttlePassMission.proto\x1a\x18\x42\x61ttlePassSchedule.proto\"\x89\x01\n\x17\x42\x61ttlePassAllDataNotify\x12(\n\x0cmission_list\x18\x01 \x03(\x0b\x32\x12.BattlePassMission\x12)\n\x0c\x63ur_schedule\x18\n \x01(\x0b\x32\x13.BattlePassSchedule\x12\x19\n\x11have_cur_schedule\x18\x03 \x01(\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BattlePassAllDataNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BATTLEPASSALLDATANOTIFY._serialized_start=85
  _BATTLEPASSALLDATANOTIFY._serialized_end=222
# @@protoc_insertion_point(module_scope)
