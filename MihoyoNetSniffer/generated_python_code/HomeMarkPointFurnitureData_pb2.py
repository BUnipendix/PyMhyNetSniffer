# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HomeMarkPointFurnitureData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HomeMarkPointNPCData_pb2 as HomeMarkPointNPCData__pb2
import HomeMarkPointSuiteData_pb2 as HomeMarkPointSuiteData__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n HomeMarkPointFurnitureData.proto\x1a\x1aHomeMarkPointNPCData.proto\x1a\x1cHomeMarkPointSuiteData.proto\x1a\x0cVector.proto\"\xd1\x01\n\x1aHomeMarkPointFurnitureData\x12\x0c\n\x04guid\x18\x01 \x01(\r\x12\x14\n\x0c\x66urniture_id\x18\x02 \x01(\r\x12\x16\n\x0e\x66urniture_type\x18\x03 \x01(\r\x12\x14\n\x03pos\x18\x04 \x01(\x0b\x32\x07.Vector\x12)\n\x08npc_data\x18\x06 \x01(\x0b\x32\x15.HomeMarkPointNPCDataH\x00\x12-\n\nsuite_data\x18\x07 \x01(\x0b\x32\x17.HomeMarkPointSuiteDataH\x00\x42\x07\n\x05\x65xtrab\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HomeMarkPointFurnitureData_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HOMEMARKPOINTFURNITUREDATA._serialized_start=109
  _HOMEMARKPOINTFURNITUREDATA._serialized_end=318
# @@protoc_insertion_point(module_scope)