# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: FurnitureMakeRsp.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import FurnitureMakeBeHelpedData_pb2 as FurnitureMakeBeHelpedData__pb2
import FurnitureMakeHelpData_pb2 as FurnitureMakeHelpData__pb2
import FurnitureMakeInfo_pb2 as FurnitureMakeInfo__pb2
import FurnitureMakeSlot_pb2 as FurnitureMakeSlot__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x46urnitureMakeRsp.proto\x1a\x1f\x46urnitureMakeBeHelpedData.proto\x1a\x1b\x46urnitureMakeHelpData.proto\x1a\x17\x46urnitureMakeInfo.proto\x1a\x17\x46urnitureMakeSlot.proto\"\xe6\x01\n\x10\x46urnitureMakeRsp\x12/\n\x13\x66urniture_make_slot\x18\r \x01(\x0b\x32\x12.FurnitureMakeSlot\x12.\n\x0ehelp_data_list\x18\x04 \x03(\x0b\x32\x16.FurnitureMakeHelpData\x12\x0f\n\x07retcode\x18\x0b \x01(\x05\x12\x34\n\x10helped_data_list\x18\x06 \x03(\x0b\x32\x1a.FurnitureMakeBeHelpedData\x12*\n\x0emake_info_list\x18\x07 \x03(\x0b\x32\x12.FurnitureMakeInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'FurnitureMakeRsp_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _FURNITUREMAKERSP._serialized_start=139
  _FURNITUREMAKERSP._serialized_end=369
# @@protoc_insertion_point(module_scope)
