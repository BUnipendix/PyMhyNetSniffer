# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OrderFinishNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ItemParam_pb2 as ItemParam__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17OrderFinishNotify.proto\x1a\x0fItemParam.proto\"\x8d\x01\n\x11OrderFinishNotify\x12\x10\n\x08order_id\x18\x03 \x01(\r\x12 \n\x18\x63\x61rd_product_remain_days\x18\x0f \x01(\r\x12\x1d\n\titem_list\x18\t \x03(\x0b\x32\n.ItemParam\x12\x11\n\tadd_mcoin\x18\x07 \x01(\r\x12\x12\n\nproduct_id\x18\x06 \x01(\tb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'OrderFinishNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ORDERFINISHNOTIFY._serialized_start=45
  _ORDERFINISHNOTIFY._serialized_end=186
# @@protoc_insertion_point(module_scope)