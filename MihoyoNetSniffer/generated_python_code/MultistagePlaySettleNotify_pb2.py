# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MultistagePlaySettleNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import InBattleChessSettleInfo_pb2 as InBattleChessSettleInfo__pb2
import InBattleMechanicusSettleInfo_pb2 as InBattleMechanicusSettleInfo__pb2
import IrodoriChessSettleInfo_pb2 as IrodoriChessSettleInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n MultistagePlaySettleNotify.proto\x1a\x1dInBattleChessSettleInfo.proto\x1a\"InBattleMechanicusSettleInfo.proto\x1a\x1cIrodoriChessSettleInfo.proto\"\x85\x02\n\x1aMultistagePlaySettleNotify\x12\x12\n\nplay_index\x18\x0e \x01(\r\x12\x10\n\x08group_id\x18\x04 \x01(\r\x12@\n\x16mechanicus_settle_info\x18\xfa\n \x01(\x0b\x32\x1d.InBattleMechanicusSettleInfoH\x00\x12\x36\n\x11\x63hess_settle_info\x18\x83\n \x01(\x0b\x32\x18.InBattleChessSettleInfoH\x00\x12=\n\x19irodori_chess_settle_info\x18\xe4\x04 \x01(\x0b\x32\x17.IrodoriChessSettleInfoH\x00\x42\x08\n\x06\x64\x65tailb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MultistagePlaySettleNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MULTISTAGEPLAYSETTLENOTIFY._serialized_start=134
  _MULTISTAGEPLAYSETTLENOTIFY._serialized_end=395
# @@protoc_insertion_point(module_scope)