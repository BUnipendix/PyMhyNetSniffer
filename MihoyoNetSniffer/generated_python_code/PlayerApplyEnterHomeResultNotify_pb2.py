# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerApplyEnterHomeResultNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&PlayerApplyEnterHomeResultNotify.proto\"\xbf\x03\n PlayerApplyEnterHomeResultNotify\x12\x12\n\ntarget_uid\x18\t \x01(\r\x12\x17\n\x0ftarget_nickname\x18\x02 \x01(\t\x12\x11\n\tis_agreed\x18\r \x01(\x08\x12\x38\n\x06reason\x18\x05 \x01(\x0e\x32(.PlayerApplyEnterHomeResultNotify.Reason\"\xa0\x02\n\x06Reason\x12\x17\n\x13REASON_PLAYER_JUDGE\x10\x00\x12%\n!REASON_PLAYER_ENTER_OPTION_REFUSE\x10\x01\x12%\n!REASON_PLAYER_ENTER_OPTION_DIRECT\x10\x02\x12\x17\n\x13REASON_SYSTEM_JUDGE\x10\x03\x12\x18\n\x14REASON_HOST_IN_MATCH\x10\x04\x12&\n\"REASON_PS_PLAYER_NOT_ACCEPT_OTHERS\x10\x05\x12\x1e\n\x1aREASON_OPEN_STATE_NOT_OPEN\x10\x06\x12\x1c\n\x18REASON_HOST_IN_EDIT_MODE\x10\x07\x12\x16\n\x12REASON_PRIOR_CHECK\x10\x08\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerApplyEnterHomeResultNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERAPPLYENTERHOMERESULTNOTIFY._serialized_start=43
  _PLAYERAPPLYENTERHOMERESULTNOTIFY._serialized_end=490
  _PLAYERAPPLYENTERHOMERESULTNOTIFY_REASON._serialized_start=202
  _PLAYERAPPLYENTERHOMERESULTNOTIFY_REASON._serialized_end=490
# @@protoc_insertion_point(module_scope)
