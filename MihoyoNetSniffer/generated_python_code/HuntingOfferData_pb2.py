# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HuntingOfferData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HuntingOfferState_pb2 as HuntingOfferState__pb2
import HuntingPair_pb2 as HuntingPair__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16HuntingOfferData.proto\x1a\x17HuntingOfferState.proto\x1a\x11HuntingPair.proto\"j\n\x10HuntingOfferData\x12\"\n\x0chunting_pair\x18\x04 \x01(\x0b\x32\x0c.HuntingPair\x12\x0f\n\x07\x63ity_id\x18\x08 \x01(\r\x12!\n\x05state\x18\x01 \x01(\x0e\x32\x12.HuntingOfferStateb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HuntingOfferData_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HUNTINGOFFERDATA._serialized_start=70
  _HUNTINGOFFERDATA._serialized_end=176
# @@protoc_insertion_point(module_scope)