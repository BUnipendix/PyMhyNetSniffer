# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CreateEntityInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CreateGadgetInfo_pb2 as CreateGadgetInfo__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x43reateEntityInfo.proto\x1a\x16\x43reateGadgetInfo.proto\x1a\x0cVector.proto\"\x9f\x02\n\x10\x43reateEntityInfo\x12\r\n\x05level\x18\x05 \x01(\r\x12\x14\n\x03pos\x18\x06 \x01(\x0b\x32\x07.Vector\x12\x14\n\x03rot\x18\x07 \x01(\x0b\x32\x07.Vector\x12\x10\n\x08scene_id\x18\n \x01(\r\x12\x0f\n\x07room_id\x18\x0b \x01(\r\x12\x18\n\x10\x63lient_unique_id\x18\x0c \x01(\r\x12\x14\n\nmonster_id\x18\x01 \x01(\rH\x00\x12\x10\n\x06npc_id\x18\x02 \x01(\rH\x00\x12\x13\n\tgadget_id\x18\x03 \x01(\rH\x00\x12\x11\n\x07item_id\x18\x04 \x01(\rH\x00\x12#\n\x06gadget\x18\r \x01(\x0b\x32\x11.CreateGadgetInfoH\x01\x42\x08\n\x06\x65ntityB\x14\n\x12\x65ntity_create_infob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CreateEntityInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEENTITYINFO._serialized_start=65
  _CREATEENTITYINFO._serialized_end=352
# @@protoc_insertion_point(module_scope)
