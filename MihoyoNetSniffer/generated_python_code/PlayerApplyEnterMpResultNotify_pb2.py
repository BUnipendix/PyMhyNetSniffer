# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerApplyEnterMpResultNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$PlayerApplyEnterMpResultNotify.proto\"\xed\x04\n\x1ePlayerApplyEnterMpResultNotify\x12\x36\n\x06reason\x18\n \x01(\x0e\x32&.PlayerApplyEnterMpResultNotify.Reason\x12\x17\n\x0ftarget_nickname\x18\x05 \x01(\t\x12\x11\n\tis_agreed\x18\x02 \x01(\x08\x12\x12\n\ntarget_uid\x18\x04 \x01(\r\"\xd2\x03\n\x06Reason\x12\x17\n\x13REASON_PLAYER_JUDGE\x10\x00\x12\x1d\n\x19REASON_SCENE_CANNOT_ENTER\x10\x01\x12!\n\x1dREASON_PLAYER_CANNOT_ENTER_MP\x10\x02\x12\x17\n\x13REASON_SYSTEM_JUDGE\x10\x03\x12\"\n\x1eREASON_ALLOW_ENTER_PLAYER_FULL\x10\x04\x12&\n\"REASON_WORLD_LEVEL_LOWER_THAN_HOST\x10\x05\x12\x18\n\x14REASON_HOST_IN_MATCH\x10\x06\x12\x1e\n\x1aREASON_PLAYER_IN_BLACKLIST\x10\x07\x12&\n\"REASON_PS_PLAYER_NOT_ACCEPT_OTHERS\x10\x08\x12\x1a\n\x16REASON_HOST_IS_BLOCKED\x10\t\x12(\n$REASON_OTHER_DATA_VERSION_NOT_LATEST\x10\n\x12\"\n\x1eREASON_DATA_VERSION_NOT_LATEST\x10\x0b\x12%\n!REASON_PLAYER_NOT_IN_PLAYER_WORLD\x10\x0c\x12\x15\n\x11REASON_MAX_PLAYER\x10\rb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerApplyEnterMpResultNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERAPPLYENTERMPRESULTNOTIFY._serialized_start=41
  _PLAYERAPPLYENTERMPRESULTNOTIFY._serialized_end=662
  _PLAYERAPPLYENTERMPRESULTNOTIFY_REASON._serialized_start=196
  _PLAYERAPPLYENTERMPRESULTNOTIFY_REASON._serialized_end=662
# @@protoc_insertion_point(module_scope)
