# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: BlitzRushActivityDetailInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BlitzRushStage_pb2 as BlitzRushStage__pb2
import ParkourLevelInfo_pb2 as ParkourLevelInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!BlitzRushActivityDetailInfo.proto\x1a\x14\x42litzRushStage.proto\x1a\x16ParkourLevelInfo.proto\"\xad\x01\n\x1b\x42litzRushActivityDetailInfo\x12#\n\nstage_list\x18\n \x03(\x0b\x32\x0f.BlitzRushStage\x12\x1a\n\x12\x63ontent_close_time\x18\x0e \x01(\r\x12\x19\n\x11is_content_closed\x18\x02 \x01(\x08\x12\x32\n\x17parkour_level_info_list\x18\x06 \x03(\x0b\x32\x11.ParkourLevelInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'BlitzRushActivityDetailInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BLITZRUSHACTIVITYDETAILINFO._serialized_start=84
  _BLITZRUSHACTIVITYDETAILINFO._serialized_end=257
# @@protoc_insertion_point(module_scope)
