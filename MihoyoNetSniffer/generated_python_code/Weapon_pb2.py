# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Weapon.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cWeapon.proto\"\x96\x01\n\x06Weapon\x12\r\n\x05level\x18\x01 \x01(\r\x12\x0b\n\x03\x65xp\x18\x02 \x01(\r\x12\x15\n\rpromote_level\x18\x03 \x01(\r\x12(\n\taffix_map\x18\x04 \x03(\x0b\x32\x15.Weapon.AffixMapEntry\x1a/\n\rAffixMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\r:\x02\x38\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Weapon_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _WEAPON_AFFIXMAPENTRY._options = None
  _WEAPON_AFFIXMAPENTRY._serialized_options = b'8\001'
  _WEAPON._serialized_start=17
  _WEAPON._serialized_end=167
  _WEAPON_AFFIXMAPENTRY._serialized_start=120
  _WEAPON_AFFIXMAPENTRY._serialized_end=167
# @@protoc_insertion_point(module_scope)
