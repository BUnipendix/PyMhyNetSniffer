# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HomeSceneArrangementInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HomeBlockArrangementInfo_pb2 as HomeBlockArrangementInfo__pb2
import HomeFurnitureData_pb2 as HomeFurnitureData__pb2
import Vector_pb2 as Vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1eHomeSceneArrangementInfo.proto\x1a\x1eHomeBlockArrangementInfo.proto\x1a\x17HomeFurnitureData.proto\x1a\x0cVector.proto\"\x97\x03\n\x18HomeSceneArrangementInfo\x12\x19\n\x08\x62orn_rot\x18\x04 \x01(\x0b\x32\x07.Vector\x12\x19\n\x08\x62orn_pos\x18\x01 \x01(\x0b\x32\x07.Vector\x12&\n\nstair_list\x18\x0b \x03(\x0b\x32\x12.HomeFurnitureData\x12%\n\tdoor_list\x18\r \x03(\x0b\x32\x12.HomeFurnitureData\x12\x17\n\x0fis_set_born_pos\x18\n \x01(\x08\x12>\n\x1b\x62lock_arrangement_info_list\x18\x08 \x03(\x0b\x32\x19.HomeBlockArrangementInfo\x12\x10\n\x08scene_id\x18\x02 \x01(\r\x12\x1b\n\x13Unk2700_BJHAMKKECEI\x18\x0c \x01(\r\x12\x1a\n\tdjinn_pos\x18\t \x01(\x0b\x32\x07.Vector\x12&\n\nmain_house\x18\x0e \x01(\x0b\x32\x12.HomeFurnitureData\x12\x15\n\rcomfort_value\x18\x07 \x01(\r\x12\x13\n\x0btmp_version\x18\x05 \x01(\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HomeSceneArrangementInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HOMESCENEARRANGEMENTINFO._serialized_start=106
  _HOMESCENEARRANGEMENTINFO._serialized_end=513
# @@protoc_insertion_point(module_scope)
