# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: source.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='source.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0csource.proto\"\xde\x01\n\x06Source\x12 \n\x07version\x18\x01 \x02(\x0e\x32\x0f.Source.Version\x12\'\n\nsourceType\x18\x02 \x02(\x0e\x32\x13.Source.SourceTypes\x12\x0e\n\x06source\x18\x03 \x02(\x0c\x12\x13\n\x0b\x63ontentType\x18\x04 \x02(\t\"*\n\x07Version\x12\x13\n\x0fUNKNOWN_VERSION\x10\x00\x12\n\n\x06_0_0_1\x10\x01\"8\n\x0bSourceTypes\x12\x17\n\x13UNKNOWN_SOURCE_TYPE\x10\x00\x12\x10\n\x0cunet_sd_hash\x10\x01')
)



_SOURCE_VERSION = _descriptor.EnumDescriptor(
  name='Version',
  full_name='Source.Version',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_VERSION', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='_0_0_1', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=139,
  serialized_end=181,
)
_sym_db.RegisterEnumDescriptor(_SOURCE_VERSION)

_SOURCE_SOURCETYPES = _descriptor.EnumDescriptor(
  name='SourceTypes',
  full_name='Source.SourceTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_SOURCE_TYPE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='unet_sd_hash', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=183,
  serialized_end=239,
)
_sym_db.RegisterEnumDescriptor(_SOURCE_SOURCETYPES)


_SOURCE = _descriptor.Descriptor(
  name='Source',
  full_name='Source',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='Source.version', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sourceType', full_name='Source.sourceType', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='Source.source', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contentType', full_name='Source.contentType', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SOURCE_VERSION,
    _SOURCE_SOURCETYPES,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=17,
  serialized_end=239,
)

_SOURCE.fields_by_name['version'].enum_type = _SOURCE_VERSION
_SOURCE.fields_by_name['sourceType'].enum_type = _SOURCE_SOURCETYPES
_SOURCE_VERSION.containing_type = _SOURCE
_SOURCE_SOURCETYPES.containing_type = _SOURCE
DESCRIPTOR.message_types_by_name['Source'] = _SOURCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Source = _reflection.GeneratedProtocolMessageType('Source', (_message.Message,), dict(
  DESCRIPTOR = _SOURCE,
  __module__ = 'source_pb2'
  # @@protoc_insertion_point(class_scope:Source)
  ))
_sym_db.RegisterMessage(Source)


# @@protoc_insertion_point(module_scope)
