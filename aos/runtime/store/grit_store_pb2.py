# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aos/runtime/store/grit_store.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\"aos/runtime/store/grit_store.proto\"T\n\x0cStoreRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x16\n\tobject_id\x18\x03 \x01(\x0cH\x00\x88\x01\x01\x12\x0c\n\x04\x64\x61ta\x18\n \x01(\x0c\x42\x0c\n\n_object_id\"4\n\rStoreResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\x0c\"2\n\x0bLoadRequest\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\x0c\"O\n\x0cLoadResponse\x12\x10\n\x08\x61gent_id\x18\x01 \x01(\x0c\x12\x11\n\tobject_id\x18\x03 \x01(\x0c\x12\x11\n\x04\x64\x61ta\x18\n \x01(\x0cH\x00\x88\x01\x01\x42\x07\n\x05_data*D\n\nObjectType\x12\x08\n\x04\x42LOB\x10\x00\x12\x08\n\x04TREE\x10\x01\x12\x0b\n\x07MESSAGE\x10\x04\x12\x0b\n\x07MAILBOX\x10\x05\x12\x08\n\x04STEP\x10\n2\\\n\tGritStore\x12(\n\x05Store\x12\r.StoreRequest\x1a\x0e.StoreResponse\"\x00\x12%\n\x04Load\x12\x0c.LoadRequest\x1a\r.LoadResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aos.runtime.store.grit_store_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_OBJECTTYPE']._serialized_start=311
  _globals['_OBJECTTYPE']._serialized_end=379
  _globals['_STOREREQUEST']._serialized_start=38
  _globals['_STOREREQUEST']._serialized_end=122
  _globals['_STORERESPONSE']._serialized_start=124
  _globals['_STORERESPONSE']._serialized_end=176
  _globals['_LOADREQUEST']._serialized_start=178
  _globals['_LOADREQUEST']._serialized_end=228
  _globals['_LOADRESPONSE']._serialized_start=230
  _globals['_LOADRESPONSE']._serialized_end=309
  _globals['_GRITSTORE']._serialized_start=381
  _globals['_GRITSTORE']._serialized_end=473
# @@protoc_insertion_point(module_scope)
