# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: EntityJumpNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x45ntityJumpNotify.proto\x1a\x0cVector.proto\"\xb6\x01\n\x10\x45ntityJumpNotify\x12)\n\tjump_type\x18\t \x01(\x0e\x32\x16.EntityJumpNotify.Type\x12\x14\n\x03rot\x18\x08 \x01(\x0b\x32\x07.Vector\x12\x14\n\x03pos\x18\n \x01(\x0b\x32\x07.Vector\x12\x11\n\tentity_id\x18\x0c \x01(\r\"8\n\x04Type\x12\r\n\tTYPE_NULL\x10\x00\x12\x0f\n\x0bTYPE_ACTIVE\x10\x01\x12\x10\n\x0cTYPE_PASSIVE\x10\x02\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'EntityJumpNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ENTITYJUMPNOTIFY._serialized_start=41
  _ENTITYJUMPNOTIFY._serialized_end=223
  _ENTITYJUMPNOTIFY_TYPE._serialized_start=167
  _ENTITYJUMPNOTIFY_TYPE._serialized_end=223
# @@protoc_insertion_point(module_scope)
