# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: HideAndSeekStageInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import HideAndSeekPlayerBattleInfo_pb2 as HideAndSeekPlayerBattleInfo__pb2
import HideAndSeekStageType_pb2 as HideAndSeekStageType__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aHideAndSeekStageInfo.proto\x1a!HideAndSeekPlayerBattleInfo.proto\x1a\x1aHideAndSeekStageType.proto\"\xad\x02\n\x14HideAndSeekStageInfo\x12\x0e\n\x06map_id\x18\x08 \x01(\r\x12\x17\n\x0fis_record_score\x18\x03 \x01(\x08\x12)\n\nstage_type\x18\x07 \x01(\x0e\x32\x15.HideAndSeekStageType\x12\x41\n\x0f\x62\x61ttle_info_map\x18\x02 \x03(\x0b\x32(.HideAndSeekStageInfo.BattleInfoMapEntry\x12\x16\n\x0ehider_uid_list\x18\x01 \x03(\r\x12\x12\n\nhunter_uid\x18\n \x01(\r\x1aR\n\x12\x42\x61ttleInfoMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12+\n\x05value\x18\x02 \x01(\x0b\x32\x1c.HideAndSeekPlayerBattleInfo:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'HideAndSeekStageInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._options = None
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._serialized_options = b'8\001'
  _HIDEANDSEEKSTAGEINFO._serialized_start=94
  _HIDEANDSEEKSTAGEINFO._serialized_end=395
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._serialized_start=313
  _HIDEANDSEEKSTAGEINFO_BATTLEINFOMAPENTRY._serialized_end=395
# @@protoc_insertion_point(module_scope)