# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: RoguelikeDungeonActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import RogueStageInfo_pb2 as RogueStageInfo__pb2
import RoguelikeShikigamiRecord_pb2 as RoguelikeShikigamiRecord__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(RoguelikeDungeonActivityDetailInfo.proto\x1a\x14RogueStageInfo.proto\x1a\x1eRoguelikeShikigamiRecord.proto\"\xe2\x01\n\"RoguelikeDungeonActivityDetailInfo\x12#\n\nstage_list\x18\x08 \x03(\x0b\x32\x0f.RogueStageInfo\x12\x31\n\x0eshikigami_list\x18\x05 \x03(\x0b\x32\x19.RoguelikeShikigamiRecord\x12\x1a\n\x12\x65quipped_rune_list\x18\x0e \x03(\r\x12\x1a\n\x12\x63ontent_close_time\x18\x06 \x01(\r\x12\x19\n\x11is_content_closed\x18\n \x01(\x08\x12\x11\n\trune_list\x18\x02 \x03(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RoguelikeDungeonActivityDetailInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ROGUELIKEDUNGEONACTIVITYDETAILINFO._serialized_start=99
  _ROGUELIKEDUNGEONACTIVITYDETAILINFO._serialized_end=325
# @@protoc_insertion_point(module_scope)