# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: NicknameSignatureAuditData.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ContentAuditAuxiliaryField_pb2 as ContentAuditAuxiliaryField__pb2
import ContentAuditField_pb2 as ContentAuditField__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n NicknameSignatureAuditData.proto\x1a ContentAuditAuxiliaryField.proto\x1a\x17\x43ontentAuditField.proto\"\xdd\x01\n\x1aNicknameSignatureAuditData\x12\x0b\n\x03\x61id\x18\x01 \x01(\t\x12\x11\n\tentity_id\x18\x02 \x01(\t\x12\x0c\n\x04lang\x18\x03 \x01(\t\x12\x11\n\tqueue_key\x18\x04 \x01(\t\x12\x0e\n\x06region\x18\x05 \x01(\t\x12\x0b\n\x03uid\x18\x06 \x01(\r\x12,\n\x10\x61udit_field_list\x18\x07 \x03(\x0b\x32\x12.ContentAuditField\x12\x33\n\x0e\x61ux_field_list\x18\x08 \x03(\x0b\x32\x1b.ContentAuditAuxiliaryFieldb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'NicknameSignatureAuditData_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NICKNAMESIGNATUREAUDITDATA._serialized_start=96
  _NICKNAMESIGNATUREAUDITDATA._serialized_end=317
# @@protoc_insertion_point(module_scope)
