# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: QueryPathRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12QueryPathRsp.proto\x1a\x0cVector.proto\"\xe5\x01\n\x0cQueryPathRsp\x12\x32\n\x0cquery_status\x18\x03 \x01(\x0e\x32\x1c.QueryPathRsp.PathStatusType\x12\x0f\n\x07retcode\x18\n \x01(\x05\x12\x10\n\x08query_id\x18\x08 \x01(\x05\x12\x18\n\x07\x63orners\x18\x01 \x03(\x0b\x32\x07.Vector\"d\n\x0ePathStatusType\x12\x19\n\x15PATH_STATUS_TYPE_FAIL\x10\x00\x12\x19\n\x15PATH_STATUS_TYPE_SUCC\x10\x01\x12\x1c\n\x18PATH_STATUS_TYPE_PARTIAL\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'QueryPathRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _QUERYPATHRSP._serialized_start=37
  _QUERYPATHRSP._serialized_end=266
  _QUERYPATHRSP_PATHSTATUSTYPE._serialized_start=166
  _QUERYPATHRSP_PATHSTATUSTYPE._serialized_end=266
# @@protoc_insertion_point(module_scope)
