# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PlayerQuitFromMpNotify.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cPlayerQuitFromMpNotify.proto\"\xe5\x03\n\x16PlayerQuitFromMpNotify\x12\x32\n\x06reason\x18\x02 \x01(\x0e\x32\".PlayerQuitFromMpNotify.QuitReason\"\x96\x03\n\nQuitReason\x12\x17\n\x13QUIT_REASON_INVALID\x10\x00\x12$\n QUIT_REASON_HOST_NO_OTHER_PLAYER\x10\x01\x12\x1c\n\x18QUIT_REASON_KICK_BY_HOST\x10\x02\x12 \n\x1cQUIT_REASON_BACK_TO_MY_WORLD\x10\x03\x12#\n\x1fQUIT_REASON_KICK_BY_HOST_LOGOUT\x10\x04\x12\"\n\x1eQUIT_REASON_KICK_BY_HOST_BLOCK\x10\x05\x12\x1a\n\x16QUIT_REASON_BE_BLOCKED\x10\x06\x12\'\n#QUIT_REASON_KICK_BY_HOST_ENTER_HOME\x10\x07\x12\"\n\x1eQUIT_REASON_HOST_SCENE_INVALID\x10\x08\x12\x1c\n\x18QUIT_REASON_KICK_BY_PLAY\x10\t\x12\x39\n5QUIT_REASON_KICK_BY_ISLAND_PARTY_GALLERY_START_FAILED\x10\nb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PlayerQuitFromMpNotify_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PLAYERQUITFROMMPNOTIFY._serialized_start=33
  _PLAYERQUITFROMMPNOTIFY._serialized_end=518
  _PLAYERQUITFROMMPNOTIFY_QUITREASON._serialized_start=112
  _PLAYERQUITFROMMPNOTIFY_QUITREASON._serialized_end=518
# @@protoc_insertion_point(module_scope)
