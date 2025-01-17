# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transaction.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tokenio.proto.extensions import field_pb2 as extensions_dot_field__pb2
import tokenio.proto.member_pb2 as member__pb2
import tokenio.proto.money_pb2 as money__pb2
import tokenio.proto.providerspecific_pb2 as providerspecific__pb2
import tokenio.proto.security_pb2 as security__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='transaction.proto',
  package='io.token.proto.common.transaction',
  syntax='proto3',
  serialized_options=_b('B\021TransactionProtos\252\002&Tokenio.Proto.Common.TransactionProtos'),
  serialized_pb=_b('\n\x11transaction.proto\x12!io.token.proto.common.transaction\x1a\x16\x65xtensions/field.proto\x1a\x0cmember.proto\x1a\x0bmoney.proto\x1a\x16providerspecific.proto\x1a\x0esecurity.proto\"\xa5\x04\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x01(\t\x12@\n\x04type\x18\x02 \x01(\x0e\x32\x32.io.token.proto.common.transaction.TransactionType\x12\x44\n\x06status\x18\x03 \x01(\x0e\x32\x34.io.token.proto.common.transaction.TransactionStatus\x12\x32\n\x06\x61mount\x18\x04 \x01(\x0b\x32\".io.token.proto.common.money.Money\x12\x19\n\x0b\x64\x65scription\x18\x05 \x01(\tB\x04\x80\xb5\x18\x01\x12\x10\n\x08token_id\x18\x06 \x01(\t\x12\x19\n\x11token_transfer_id\x18\x07 \x01(\t\x12\x15\n\rcreated_at_ms\x18\x08 \x01(\x03\x12T\n\x08metadata\x18\t \x03(\x0b\x32<.io.token.proto.common.transaction.Transaction.MetadataEntryB\x04\x80\xb5\x18\x01\x12h\n\x1cprovider_transaction_details\x18\n \x01(\x0b\x32\x42.io.token.proto.common.providerspecific.ProviderTransactionDetails\x1a/\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xda\x02\n\x07\x42\x61lance\x12\x12\n\naccount_id\x18\x01 \x01(\t\x12\x33\n\x07\x63urrent\x18\x02 \x01(\x0b\x32\".io.token.proto.common.money.Money\x12\x35\n\tavailable\x18\x03 \x01(\x0b\x32\".io.token.proto.common.money.Money\x12\x15\n\rupdated_at_ms\x18\x04 \x01(\x03\x12O\n\x0eother_balances\x18\x05 \x03(\x0b\x32\x37.io.token.proto.common.transaction.Balance.TypedBalance\x1ag\n\x0cTypedBalance\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\x32\n\x06\x61mount\x18\x02 \x01(\x0b\x32\".io.token.proto.common.money.Money\x12\x15\n\rupdated_at_ms\x18\x03 \x01(\x03*:\n\x0fTransactionType\x12\x10\n\x0cINVALID_TYPE\x10\x00\x12\t\n\x05\x44\x45\x42IT\x10\x01\x12\n\n\x06\x43REDIT\x10\x02*\xfd\x02\n\x11TransactionStatus\x12\x12\n\x0eINVALID_STATUS\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0e\n\nPROCESSING\x10\x07\x12\x0b\n\x07SUCCESS\x10\x02\x12\"\n\x1ePENDING_EXTERNAL_AUTHORIZATION\x10\x0f\x12\x14\n\x10\x46\x41ILURE_CANCELED\x10\n\x12\x1e\n\x1a\x46\x41ILURE_INSUFFICIENT_FUNDS\x10\x03\x12\x1c\n\x18\x46\x41ILURE_INVALID_CURRENCY\x10\x04\x12\x1d\n\x19\x46\x41ILURE_PERMISSION_DENIED\x10\x06\x12\x19\n\x15\x46\x41ILURE_QUOTE_EXPIRED\x10\x0b\x12\x1a\n\x16\x46\x41ILURE_INVALID_AMOUNT\x10\x0c\x12\x19\n\x15\x46\x41ILURE_INVALID_QUOTE\x10\r\x12\x13\n\x0f\x46\x41ILURE_EXPIRED\x10\x0e\x12\x13\n\x0f\x46\x41ILURE_GENERIC\x10\x05\x12\x08\n\x04SENT\x10\x10\x12\r\n\tINITIATED\x10\x11*X\n\rRequestStatus\x12\x13\n\x0fINVALID_REQUEST\x10\x00\x12\x16\n\x12SUCCESSFUL_REQUEST\x10\x01\x12\x1a\n\x16MORE_SIGNATURES_NEEDED\x10\x02\x42<B\x11TransactionProtos\xaa\x02&Tokenio.Proto.Common.TransactionProtosb\x06proto3')
  ,
  dependencies=[extensions_dot_field__pb2.DESCRIPTOR,member__pb2.DESCRIPTOR,money__pb2.DESCRIPTOR,providerspecific__pb2.DESCRIPTOR,security__pb2.DESCRIPTOR,])

_TRANSACTIONTYPE = _descriptor.EnumDescriptor(
  name='TransactionType',
  full_name='io.token.proto.common.transaction.TransactionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEBIT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREDIT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1048,
  serialized_end=1106,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONTYPE)

TransactionType = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONTYPE)
_TRANSACTIONSTATUS = _descriptor.EnumDescriptor(
  name='TransactionStatus',
  full_name='io.token.proto.common.transaction.TransactionStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_STATUS', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PROCESSING', index=2, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=3, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PENDING_EXTERNAL_AUTHORIZATION', index=4, number=15,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_CANCELED', index=5, number=10,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_INSUFFICIENT_FUNDS', index=6, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_INVALID_CURRENCY', index=7, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_PERMISSION_DENIED', index=8, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_QUOTE_EXPIRED', index=9, number=11,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_INVALID_AMOUNT', index=10, number=12,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_INVALID_QUOTE', index=11, number=13,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_EXPIRED', index=12, number=14,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE_GENERIC', index=13, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SENT', index=14, number=16,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INITIATED', index=15, number=17,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1109,
  serialized_end=1490,
)
_sym_db.RegisterEnumDescriptor(_TRANSACTIONSTATUS)

TransactionStatus = enum_type_wrapper.EnumTypeWrapper(_TRANSACTIONSTATUS)
_REQUESTSTATUS = _descriptor.EnumDescriptor(
  name='RequestStatus',
  full_name='io.token.proto.common.transaction.RequestStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_REQUEST', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESSFUL_REQUEST', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MORE_SIGNATURES_NEEDED', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1492,
  serialized_end=1580,
)
_sym_db.RegisterEnumDescriptor(_REQUESTSTATUS)

RequestStatus = enum_type_wrapper.EnumTypeWrapper(_REQUESTSTATUS)
INVALID_TYPE = 0
DEBIT = 1
CREDIT = 2
INVALID_STATUS = 0
PENDING = 1
PROCESSING = 7
SUCCESS = 2
PENDING_EXTERNAL_AUTHORIZATION = 15
FAILURE_CANCELED = 10
FAILURE_INSUFFICIENT_FUNDS = 3
FAILURE_INVALID_CURRENCY = 4
FAILURE_PERMISSION_DENIED = 6
FAILURE_QUOTE_EXPIRED = 11
FAILURE_INVALID_AMOUNT = 12
FAILURE_INVALID_QUOTE = 13
FAILURE_EXPIRED = 14
FAILURE_GENERIC = 5
SENT = 16
INITIATED = 17
INVALID_REQUEST = 0
SUCCESSFUL_REQUEST = 1
MORE_SIGNATURES_NEEDED = 2



_TRANSACTION_METADATAENTRY = _descriptor.Descriptor(
  name='MetadataEntry',
  full_name='io.token.proto.common.transaction.Transaction.MetadataEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='io.token.proto.common.transaction.Transaction.MetadataEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='io.token.proto.common.transaction.Transaction.MetadataEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=650,
  serialized_end=697,
)

_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='io.token.proto.common.transaction.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='io.token.proto.common.transaction.Transaction.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='io.token.proto.common.transaction.Transaction.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='io.token.proto.common.transaction.Transaction.status', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='io.token.proto.common.transaction.Transaction.amount', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='io.token.proto.common.transaction.Transaction.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_id', full_name='io.token.proto.common.transaction.Transaction.token_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='token_transfer_id', full_name='io.token.proto.common.transaction.Transaction.token_transfer_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at_ms', full_name='io.token.proto.common.transaction.Transaction.created_at_ms', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='io.token.proto.common.transaction.Transaction.metadata', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\200\265\030\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='provider_transaction_details', full_name='io.token.proto.common.transaction.Transaction.provider_transaction_details', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_TRANSACTION_METADATAENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=697,
)


_BALANCE_TYPEDBALANCE = _descriptor.Descriptor(
  name='TypedBalance',
  full_name='io.token.proto.common.transaction.Balance.TypedBalance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='io.token.proto.common.transaction.Balance.TypedBalance.type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='io.token.proto.common.transaction.Balance.TypedBalance.amount', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at_ms', full_name='io.token.proto.common.transaction.Balance.TypedBalance.updated_at_ms', index=2,
      number=3, type=3, cpp_type=2, label=1,
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
  serialized_start=943,
  serialized_end=1046,
)

_BALANCE = _descriptor.Descriptor(
  name='Balance',
  full_name='io.token.proto.common.transaction.Balance',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account_id', full_name='io.token.proto.common.transaction.Balance.account_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current', full_name='io.token.proto.common.transaction.Balance.current', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='available', full_name='io.token.proto.common.transaction.Balance.available', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='updated_at_ms', full_name='io.token.proto.common.transaction.Balance.updated_at_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='other_balances', full_name='io.token.proto.common.transaction.Balance.other_balances', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_BALANCE_TYPEDBALANCE, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=700,
  serialized_end=1046,
)

_TRANSACTION_METADATAENTRY.containing_type = _TRANSACTION
_TRANSACTION.fields_by_name['type'].enum_type = _TRANSACTIONTYPE
_TRANSACTION.fields_by_name['status'].enum_type = _TRANSACTIONSTATUS
_TRANSACTION.fields_by_name['amount'].message_type = money__pb2._MONEY
_TRANSACTION.fields_by_name['metadata'].message_type = _TRANSACTION_METADATAENTRY
_TRANSACTION.fields_by_name['provider_transaction_details'].message_type = providerspecific__pb2._PROVIDERTRANSACTIONDETAILS
_BALANCE_TYPEDBALANCE.fields_by_name['amount'].message_type = money__pb2._MONEY
_BALANCE_TYPEDBALANCE.containing_type = _BALANCE
_BALANCE.fields_by_name['current'].message_type = money__pb2._MONEY
_BALANCE.fields_by_name['available'].message_type = money__pb2._MONEY
_BALANCE.fields_by_name['other_balances'].message_type = _BALANCE_TYPEDBALANCE
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['Balance'] = _BALANCE
DESCRIPTOR.enum_types_by_name['TransactionType'] = _TRANSACTIONTYPE
DESCRIPTOR.enum_types_by_name['TransactionStatus'] = _TRANSACTIONSTATUS
DESCRIPTOR.enum_types_by_name['RequestStatus'] = _REQUESTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), {

  'MetadataEntry' : _reflection.GeneratedProtocolMessageType('MetadataEntry', (_message.Message,), {
    'DESCRIPTOR' : _TRANSACTION_METADATAENTRY,
    '__module__' : 'transaction_pb2'
    # @@protoc_insertion_point(class_scope:io.token.proto.common.transaction.Transaction.MetadataEntry)
    })
  ,
  'DESCRIPTOR' : _TRANSACTION,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.transaction.Transaction)
  })
_sym_db.RegisterMessage(Transaction)
_sym_db.RegisterMessage(Transaction.MetadataEntry)

Balance = _reflection.GeneratedProtocolMessageType('Balance', (_message.Message,), {

  'TypedBalance' : _reflection.GeneratedProtocolMessageType('TypedBalance', (_message.Message,), {
    'DESCRIPTOR' : _BALANCE_TYPEDBALANCE,
    '__module__' : 'transaction_pb2'
    # @@protoc_insertion_point(class_scope:io.token.proto.common.transaction.Balance.TypedBalance)
    })
  ,
  'DESCRIPTOR' : _BALANCE,
  '__module__' : 'transaction_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.transaction.Balance)
  })
_sym_db.RegisterMessage(Balance)
_sym_db.RegisterMessage(Balance.TypedBalance)


DESCRIPTOR._options = None
_TRANSACTION_METADATAENTRY._options = None
_TRANSACTION.fields_by_name['description']._options = None
_TRANSACTION.fields_by_name['metadata']._options = None
# @@protoc_insertion_point(module_scope)
