# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Investigation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13Investigation.proto\"\xc9\x01\n\rInvestigation\x12\x16\n\x0etotal_progress\x18\x05 \x01(\r\x12#\n\x05state\x18\x02 \x01(\x0e\x32\x14.Investigation.State\x12\x10\n\x08progress\x18\r \x01(\r\x12\n\n\x02id\x18\t \x01(\r\"]\n\x05State\x12\x11\n\rSTATE_INVALID\x10\x00\x12\x15\n\x11STATE_IN_PROGRESS\x10\x01\x12\x12\n\x0eSTATE_COMPLETE\x10\x02\x12\x16\n\x12STATE_REWARD_TAKEN\x10\x03\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Investigation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _INVESTIGATION._serialized_start=24
  _INVESTIGATION._serialized_end=225
  _INVESTIGATION_STATE._serialized_start=132
  _INVESTIGATION_STATE._serialized_end=225
# @@protoc_insertion_point(module_scope)
