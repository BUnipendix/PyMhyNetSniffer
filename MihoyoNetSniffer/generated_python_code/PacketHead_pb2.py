# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: PacketHead.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10PacketHead.proto\"\xc8\x04\n\nPacketHead\x12\x11\n\tpacket_id\x18\x01 \x01(\r\x12\x0e\n\x06rpc_id\x18\x02 \x01(\r\x12\x1a\n\x12\x63lient_sequence_id\x18\x03 \x01(\r\x12\x17\n\x0f\x65net_channel_id\x18\x04 \x01(\r\x12\x18\n\x10\x65net_is_reliable\x18\x05 \x01(\r\x12\x0f\n\x07sent_ms\x18\x06 \x01(\x04\x12\x0f\n\x07user_id\x18\x0b \x01(\r\x12\x0f\n\x07user_ip\x18\x0c \x01(\r\x12\x17\n\x0fuser_session_id\x18\r \x01(\r\x12\x14\n\x0crecv_time_ms\x18\x15 \x01(\x04\x12\x19\n\x11rpc_begin_time_ms\x18\x16 \x01(\r\x12(\n\x07\x65xt_map\x18\x17 \x03(\x0b\x32\x17.PacketHead.ExtMapEntry\x12\x15\n\rsender_app_id\x18\x18 \x01(\r\x12\x16\n\x0esource_service\x18\x1f \x01(\r\x12\x16\n\x0etarget_service\x18  \x01(\r\x12<\n\x12service_app_id_map\x18! \x03(\x0b\x32 .PacketHead.ServiceAppIdMapEntry\x12\x1a\n\x12is_set_game_thread\x18\" \x01(\x08\x12\x19\n\x11game_thread_index\x18# \x01(\r\x1a-\n\x0b\x45xtMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x1a\x36\n\x14ServiceAppIdMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PacketHead_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PACKETHEAD_EXTMAPENTRY._options = None
  _PACKETHEAD_EXTMAPENTRY._serialized_options = b'8\001'
  _PACKETHEAD_SERVICEAPPIDMAPENTRY._options = None
  _PACKETHEAD_SERVICEAPPIDMAPENTRY._serialized_options = b'8\001'
  _PACKETHEAD._serialized_start=21
  _PACKETHEAD._serialized_end=605
  _PACKETHEAD_EXTMAPENTRY._serialized_start=504
  _PACKETHEAD_EXTMAPENTRY._serialized_end=549
  _PACKETHEAD_SERVICEAPPIDMAPENTRY._serialized_start=551
  _PACKETHEAD_SERVICEAPPIDMAPENTRY._serialized_end=605
# @@protoc_insertion_point(module_scope)
