# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Shop.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import ShopCardProduct_pb2 as ShopCardProduct__pb2
import ShopConcertProduct_pb2 as ShopConcertProduct__pb2
import ShopGoods_pb2 as ShopGoods__pb2
import ShopMcoinProduct_pb2 as ShopMcoinProduct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nShop.proto\x1a\x15ShopCardProduct.proto\x1a\x18ShopConcertProduct.proto\x1a\x0fShopGoods.proto\x1a\x16ShopMcoinProduct.proto\"\x93\x02\n\x04Shop\x12\x11\n\tshop_type\x18\x01 \x01(\r\x12\x19\n\x11next_refresh_time\x18\x05 \x01(\r\x12\x0f\n\x07\x63ity_id\x18\x0c \x01(\r\x12\x1d\n\x15\x63ity_reputation_level\x18\x08 \x01(\r\x12\x1e\n\ngoods_list\x18\x03 \x03(\x0b\x32\n.ShopGoods\x12+\n\x11\x63\x61rd_product_list\x18\x0b \x03(\x0b\x32\x10.ShopCardProduct\x12\x31\n\x14\x63oncert_product_list\x18\t \x03(\x0b\x32\x13.ShopConcertProduct\x12-\n\x12mcoin_product_list\x18\x07 \x03(\x0b\x32\x11.ShopMcoinProductb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Shop_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SHOP._serialized_start=105
  _SHOP._serialized_end=380
# @@protoc_insertion_point(module_scope)
