# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: extensions/message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='extensions/message.proto',
  package='io.token.proto.extensions.message',
  syntax='proto3',
  serialized_options=_b('B\021MessageExtensions'),
  serialized_pb=_b('\n\x18\x65xtensions/message.proto\x12!io.token.proto.extensions.message\x1a google/protobuf/descriptor.proto:1\n\x06redact\x12\x1f.google.protobuf.MessageOptions\x18\xd0\x86\x03 \x01(\x08\x42\x13\x42\x11MessageExtensionsb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])


REDACT_FIELD_NUMBER = 50000
redact = _descriptor.FieldDescriptor(
  name='redact', full_name='io.token.proto.extensions.message.redact', index=0,
  number=50000, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)

DESCRIPTOR.extensions_by_name['redact'] = redact
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(redact)

DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)