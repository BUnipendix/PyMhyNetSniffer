# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MultistagePlayInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import BrickBreakerStageInfo_pb2 as BrickBreakerStageInfo__pb2
import CharAmusementInfo_pb2 as CharAmusementInfo__pb2
import CoinCollectStageInfo_pb2 as CoinCollectStageInfo__pb2
import HideAndSeekStageInfo_pb2 as HideAndSeekStageInfo__pb2
import InBattleChessInfo_pb2 as InBattleChessInfo__pb2
import InBattleFleurFairInfo_pb2 as InBattleFleurFairInfo__pb2
import InBattleIrodoriChessInfo_pb2 as InBattleIrodoriChessInfo__pb2
import InBattleMechanicusInfo_pb2 as InBattleMechanicusInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18MultistagePlayInfo.proto\x1a\x1b\x42rickBreakerStageInfo.proto\x1a\x17\x43harAmusementInfo.proto\x1a\x1a\x43oinCollectStageInfo.proto\x1a\x1aHideAndSeekStageInfo.proto\x1a\x17InBattleChessInfo.proto\x1a\x1bInBattleFleurFairInfo.proto\x1a\x1eInBattleIrodoriChessInfo.proto\x1a\x1cInBattleMechanicusInfo.proto\"\xca\x04\n\x12MultistagePlayInfo\x12\x12\n\nplay_index\x18\r \x01(\r\x12\x10\n\x08\x64uration\x18\x02 \x01(\r\x12\x12\n\nstage_type\x18\x05 \x01(\r\x12\x10\n\x08group_id\x18\x01 \x01(\r\x12\x13\n\x0bstage_index\x18\n \x01(\r\x12\x12\n\nbegin_time\x18\t \x01(\r\x12\x11\n\tplay_type\x18\x0f \x01(\r\x12\x33\n\x0fmechanicus_info\x18\x97\n \x01(\x0b\x32\x17.InBattleMechanicusInfoH\x00\x12\x32\n\x0f\x66leur_fair_info\x18\xde\x0b \x01(\x0b\x32\x16.InBattleFleurFairInfoH\x00\x12\x34\n\x12hide_and_seek_info\x18\xbd\r \x01(\x0b\x32\x15.HideAndSeekStageInfoH\x00\x12)\n\nchess_info\x18\xdc\r \x01(\x0b\x32\x12.InBattleChessInfoH\x00\x12\x38\n\x12irodori_chess_info\x18\xab\x0e \x01(\x0b\x32\x19.InBattleIrodoriChessInfoH\x00\x12\x32\n\x13\x63har_amusement_info\x18\xf7\x07 \x01(\x0b\x32\x12.CharAmusementInfoH\x00\x12\x35\n\x12\x62rick_breaker_info\x18\xa3\x04 \x01(\x0b\x32\x16.BrickBreakerStageInfoH\x00\x12\x33\n\x11\x63oin_collect_info\x18\xef\t \x01(\x0b\x32\x15.CoinCollectStageInfoH\x00\x42\x08\n\x06\x64\x65tailb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'MultistagePlayInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MULTISTAGEPLAYINFO._serialized_start=255
  _MULTISTAGEPLAYINFO._serialized_end=841
# @@protoc_insertion_point(module_scope)
