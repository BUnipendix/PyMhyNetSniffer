# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: VehicleInteractRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import VehicleInteractType_pb2 as VehicleInteractType__pb2
import VehicleMember_pb2 as VehicleMember__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18VehicleInteractRsp.proto\x1a\x19VehicleInteractType.proto\x1a\x13VehicleMember.proto\"\x85\x01\n\x12VehicleInteractRsp\x12+\n\rinteract_type\x18\x0f \x01(\x0e\x32\x14.VehicleInteractType\x12\x1e\n\x06member\x18\x03 \x01(\x0b\x32\x0e.VehicleMember\x12\x11\n\tentity_id\x18\x02 \x01(\r\x12\x0f\n\x07retcode\x18\x01 \x01(\x05\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'VehicleInteractRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VEHICLEINTERACTRSP._serialized_start=77
  _VEHICLEINTERACTRSP._serialized_end=210
# @@protoc_insertion_point(module_scope)