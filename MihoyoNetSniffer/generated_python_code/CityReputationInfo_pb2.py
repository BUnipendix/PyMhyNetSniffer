# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CityReputationInfo.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CityReputationExploreInfo_pb2 as CityReputationExploreInfo__pb2
import CityReputationHuntInfo_pb2 as CityReputationHuntInfo__pb2
import CityReputationQuestInfo_pb2 as CityReputationQuestInfo__pb2
import CityReputationRequestInfo_pb2 as CityReputationRequestInfo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x43ityReputationInfo.proto\x1a\x1f\x43ityReputationExploreInfo.proto\x1a\x1c\x43ityReputationHuntInfo.proto\x1a\x1d\x43ityReputationQuestInfo.proto\x1a\x1f\x43ityReputationRequestInfo.proto\"\xcc\x02\n\x12\x43ityReputationInfo\x12\r\n\x05level\x18\x04 \x01(\r\x12\x19\n\x11next_refresh_time\x18\x03 \x01(\r\x12*\n\thunt_info\x18\x0b \x01(\x0b\x32\x17.CityReputationHuntInfo\x12\x1f\n\x17taken_level_reward_list\x18\x02 \x03(\r\x12 \n\x18total_accept_request_num\x18\x06 \x01(\r\x12\x30\n\x0crequest_info\x18\x05 \x01(\x0b\x32\x1a.CityReputationRequestInfo\x12,\n\nquest_info\x18\t \x01(\x0b\x32\x18.CityReputationQuestInfo\x12\x0b\n\x03\x65xp\x18\r \x01(\r\x12\x30\n\x0c\x65xplore_info\x18\n \x01(\x0b\x32\x1a.CityReputationExploreInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CityReputationInfo_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CITYREPUTATIONINFO._serialized_start=156
  _CITYREPUTATIONINFO._serialized_end=488
# @@protoc_insertion_point(module_scope)
