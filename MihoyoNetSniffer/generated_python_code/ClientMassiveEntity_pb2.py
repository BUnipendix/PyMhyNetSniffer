# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ClientMassiveEntity.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import MassiveBoxInfo_pb2 as MassiveBoxInfo__pb2
import MassiveGrassInfo_pb2 as MassiveGrassInfo__pb2
import MassiveWaterInfo_pb2 as MassiveWaterInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x43lientMassiveEntity.proto\x1a\x14MassiveBoxInfo.proto\x1a\x16MassiveGrassInfo.proto\x1a\x16MassiveWaterInfo.proto\"\xd3\x01\n\x13\x43lientMassiveEntity\x12\x13\n\x0b\x65ntity_type\x18\x01 \x01(\r\x12\x11\n\tconfig_id\x18\x02 \x01(\r\x12\x0e\n\x06obj_id\x18\x03 \x01(\x03\x12\'\n\nwater_info\x18\x04 \x01(\x0b\x32\x11.MassiveWaterInfoH\x00\x12\'\n\ngrass_info\x18\x05 \x01(\x0b\x32\x11.MassiveGrassInfoH\x00\x12#\n\x08\x62ox_info\x18\x06 \x01(\x0b\x32\x0f.MassiveBoxInfoH\x00\x42\r\n\x0b\x65ntity_infob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ClientMassiveEntity_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CLIENTMASSIVEENTITY._serialized_start=100
  _CLIENTMASSIVEENTITY._serialized_end=311
# @@protoc_insertion_point(module_scope)