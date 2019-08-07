# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: eidas.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import tokenio.proto.alias_pb2 as alias__pb2
import tokenio.proto.security_pb2 as security__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='eidas.proto',
  package='io.token.proto.common.eidas',
  syntax='proto3',
  serialized_options=_b('B\013EidasProtos\252\002 Tokenio.Proto.Common.EidasProtos'),
  serialized_pb=_b('\n\x0b\x65idas.proto\x12\x1bio.token.proto.common.eidas\x1a\x0b\x61lias.proto\x1a\x0esecurity.proto\"\x97\x01\n\x12VerifyEidasPayload\x12\x11\n\tmember_id\x18\x01 \x01(\t\x12\x17\n\x0f\x66i_reference_id\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x03 \x01(\t\x12@\n\talgorithm\x18\x04 \x01(\x0e\x32-.io.token.proto.common.security.Key.AlgorithmB0B\x0b\x45idasProtos\xaa\x02 Tokenio.Proto.Common.EidasProtosb\x06proto3')
  ,
  dependencies=[alias__pb2.DESCRIPTOR,security__pb2.DESCRIPTOR,])




_VERIFYEIDASPAYLOAD = _descriptor.Descriptor(
  name='VerifyEidasPayload',
  full_name='io.token.proto.common.eidas.VerifyEidasPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='member_id', full_name='io.token.proto.common.eidas.VerifyEidasPayload.member_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fi_reference_id', full_name='io.token.proto.common.eidas.VerifyEidasPayload.fi_reference_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate', full_name='io.token.proto.common.eidas.VerifyEidasPayload.certificate', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='algorithm', full_name='io.token.proto.common.eidas.VerifyEidasPayload.algorithm', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=225,
)

_VERIFYEIDASPAYLOAD.fields_by_name['algorithm'].enum_type = security__pb2._KEY_ALGORITHM
DESCRIPTOR.message_types_by_name['VerifyEidasPayload'] = _VERIFYEIDASPAYLOAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VerifyEidasPayload = _reflection.GeneratedProtocolMessageType('VerifyEidasPayload', (_message.Message,), {
  'DESCRIPTOR' : _VERIFYEIDASPAYLOAD,
  '__module__' : 'eidas_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.eidas.VerifyEidasPayload)
  })
_sym_db.RegisterMessage(VerifyEidasPayload)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)