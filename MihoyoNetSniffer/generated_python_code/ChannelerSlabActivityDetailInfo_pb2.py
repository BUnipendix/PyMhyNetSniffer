# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ChannelerSlabActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ChannelerSlabBuffInfo_pb2 as ChannelerSlabBuffInfo__pb2
import ChannelerSlabChallengeStage_pb2 as ChannelerSlabChallengeStage__pb2
import ChannelerSlabLoopDungeonStageInfo_pb2 as ChannelerSlabLoopDungeonStageInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ChannelerSlabActivityDetailInfo.proto\x1a\x1b\x43hannelerSlabBuffInfo.proto\x1a!ChannelerSlabChallengeStage.proto\x1a\'ChannelerSlabLoopDungeonStageInfo.proto\"\xda\x01\n\x1f\x43hannelerSlabActivityDetailInfo\x12\x43\n\x17loop_dungeon_stage_info\x18\x02 \x01(\x0b\x32\".ChannelerSlabLoopDungeonStageInfo\x12)\n\tbuff_info\x18\t \x01(\x0b\x32\x16.ChannelerSlabBuffInfo\x12\x30\n\nstage_list\x18\x08 \x03(\x0b\x32\x1c.ChannelerSlabChallengeStage\x12\x15\n\rplay_end_time\x18\x0e \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChannelerSlabActivityDetailInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CHANNELERSLABACTIVITYDETAILINFO._serialized_start=147
  _CHANNELERSLABACTIVITYDETAILINFO._serialized_end=365
# @@protoc_insertion_point(module_scope)
