# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: providerspecific.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tokenio.proto.extensions import message_pb2 as extensions_dot_message__pb2
import tokenio.proto.address_pb2 as address__pb2
import tokenio.proto.polishapi_pb2 as polishapi__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='providerspecific.proto',
  package='io.token.proto.common.providerspecific',
  syntax='proto3',
  serialized_options=_b('B\020ProviderSpecific\252\002%Tokenio.Proto.Common.ProviderSpecific'),
  serialized_pb=_b('\n\x16providerspecific.proto\x12&io.token.proto.common.providerspecific\x1a\x18\x65xtensions/message.proto\x1a\raddress.proto\x1a\x0fpolishapi.proto\"\xf0\x01\n\x16ProviderAccountDetails\x12Z\n\x14\x63ma9_account_details\x18\x01 \x01(\x0b\x32:.io.token.proto.common.providerspecific.Cma9AccountDetailsH\x00\x12o\n\x1apolish_api_account_details\x18\x02 \x01(\x0b\x32I.io.token.proto.common.providerspecific.polishapi.PolishApiAccountDetailsH\x00\x42\t\n\x07\x64\x65tails\"\xa0\x01\n\x1aProviderTransactionDetails\x12w\n\x1epolish_api_transaction_details\x18\x01 \x01(\x0b\x32M.io.token.proto.common.providerspecific.polishapi.PolishApiTransactionDetailsH\x00\x42\t\n\x07\x64\x65tails\"\x9b\x01\n\x18ProviderTransferMetadata\x12s\n\x1cpolish_api_transfer_metadata\x18\x01 \x01(\x0b\x32K.io.token.proto.common.providerspecific.polishapi.PolishApiTransferMetadataH\x00\x42\n\n\x08metadata\"\x9d\t\n\x12\x43ma9AccountDetails\x12\x10\n\x08party_id\x18\x01 \x01(\t\x12\x14\n\x0cparty_number\x18\x02 \x01(\t\x12X\n\nparty_type\x18\x03 \x01(\x0e\x32\x44.io.token.proto.common.providerspecific.Cma9AccountDetails.PartyType\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x15\n\remail_address\x18\x05 \x01(\t\x12\r\n\x05phone\x18\x06 \x01(\t\x12\x0e\n\x06mobile\x18\x07 \x01(\t\x12W\n\x07\x61\x64\x64ress\x18\x08 \x03(\x0b\x32\x46.io.token.proto.common.providerspecific.Cma9AccountDetails.Cma9Address\x12\\\n\x0c\x61\x63\x63ount_type\x18\t \x01(\x0e\x32\x46.io.token.proto.common.providerspecific.Cma9AccountDetails.AccountType\x12\x62\n\x0f\x61\x63\x63ount_subtype\x18\n \x01(\x0e\x32I.io.token.proto.common.providerspecific.Cma9AccountDetails.AccountSubtype\x12\x13\n\x0b\x64\x65scription\x18\x0b \x01(\t\x1a\xa4\x01\n\x0b\x43ma9Address\x12\\\n\x0c\x61\x64\x64ress_type\x18\x01 \x01(\x0e\x32\x46.io.token.proto.common.providerspecific.Cma9AccountDetails.AddressType\x12\x37\n\x07\x61\x64\x64ress\x18\x02 \x01(\x0b\x32&.io.token.proto.common.address.Address\"F\n\tPartyType\x12\x16\n\x12INVALID_PARTY_TYPE\x10\x00\x12\x0c\n\x08\x44\x45LEGATE\x10\x01\x12\t\n\x05JOINT\x10\x02\x12\x08\n\x04SOLE\x10\x03\"\x9c\x01\n\x0b\x41\x64\x64ressType\x12\x18\n\x14INVALID_ADDRESS_TYPE\x10\x00\x12\x0c\n\x08\x42USINESS\x10\x01\x12\x12\n\x0e\x43ORRESPONDENCE\x10\x02\x12\x0e\n\nDELIVERYTO\x10\x03\x12\n\n\x06MAILTO\x10\x04\x12\t\n\x05POBOX\x10\x05\x12\n\n\x06POSTAL\x10\x06\x12\x0f\n\x0bRESIDENTIAL\x10\x07\x12\r\n\tSTATEMENT\x10\x08\"S\n\x0b\x41\x63\x63ountType\x12\x18\n\x14INVALID_ACCOUNT_TYPE\x10\x00\x12\x14\n\x10\x42USINESS_ACCOUNT\x10\x01\x12\x14\n\x10PERSONAL_ACCOUNT\x10\x02\"\xa7\x01\n\x0e\x41\x63\x63ountSubtype\x12\x1b\n\x17INVALID_ACCOUNT_SUBTYPE\x10\x00\x12\x0f\n\x0b\x43HARGE_CARD\x10\x01\x12\x0f\n\x0b\x43REDIT_CARD\x10\x02\x12\x13\n\x0f\x43URRENT_ACCOUNT\x10\x03\x12\n\n\x06\x45MONEY\x10\x04\x12\x08\n\x04LOAN\x10\x05\x12\x0c\n\x08MORTGAGE\x10\x06\x12\x10\n\x0cPREPAID_CARD\x10\x07\x12\x0b\n\x07SAVINGS\x10\x08:\x04\x80\xb5\x18\x01\x42:B\x10ProviderSpecific\xaa\x02%Tokenio.Proto.Common.ProviderSpecificb\x06proto3')
  ,
  dependencies=[extensions_dot_message__pb2.DESCRIPTOR,address__pb2.DESCRIPTOR,polishapi__pb2.DESCRIPTOR,])



_CMA9ACCOUNTDETAILS_PARTYTYPE = _descriptor.EnumDescriptor(
  name='PartyType',
  full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.PartyType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_PARTY_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELEGATE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='JOINT', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SOLE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1380,
  serialized_end=1450,
)
_sym_db.RegisterEnumDescriptor(_CMA9ACCOUNTDETAILS_PARTYTYPE)

_CMA9ACCOUNTDETAILS_ADDRESSTYPE = _descriptor.EnumDescriptor(
  name='AddressType',
  full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.AddressType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_ADDRESS_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSINESS', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CORRESPONDENCE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELIVERYTO', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MAILTO', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POBOX', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POSTAL', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESIDENTIAL', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATEMENT', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1453,
  serialized_end=1609,
)
_sym_db.RegisterEnumDescriptor(_CMA9ACCOUNTDETAILS_ADDRESSTYPE)

_CMA9ACCOUNTDETAILS_ACCOUNTTYPE = _descriptor.EnumDescriptor(
  name='AccountType',
  full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.AccountType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_ACCOUNT_TYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUSINESS_ACCOUNT', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSONAL_ACCOUNT', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1611,
  serialized_end=1694,
)
_sym_db.RegisterEnumDescriptor(_CMA9ACCOUNTDETAILS_ACCOUNTTYPE)

_CMA9ACCOUNTDETAILS_ACCOUNTSUBTYPE = _descriptor.EnumDescriptor(
  name='AccountSubtype',
  full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.AccountSubtype',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID_ACCOUNT_SUBTYPE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHARGE_CARD', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CREDIT_CARD', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CURRENT_ACCOUNT', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMONEY', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOAN', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MORTGAGE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PREPAID_CARD', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SAVINGS', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1697,
  serialized_end=1864,
)
_sym_db.RegisterEnumDescriptor(_CMA9ACCOUNTDETAILS_ACCOUNTSUBTYPE)


_PROVIDERACCOUNTDETAILS = _descriptor.Descriptor(
  name='ProviderAccountDetails',
  full_name='io.token.proto.common.providerspecific.ProviderAccountDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cma9_account_details', full_name='io.token.proto.common.providerspecific.ProviderAccountDetails.cma9_account_details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='polish_api_account_details', full_name='io.token.proto.common.providerspecific.ProviderAccountDetails.polish_api_account_details', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='details', full_name='io.token.proto.common.providerspecific.ProviderAccountDetails.details',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=125,
  serialized_end=365,
)


_PROVIDERTRANSACTIONDETAILS = _descriptor.Descriptor(
  name='ProviderTransactionDetails',
  full_name='io.token.proto.common.providerspecific.ProviderTransactionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='polish_api_transaction_details', full_name='io.token.proto.common.providerspecific.ProviderTransactionDetails.polish_api_transaction_details', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='details', full_name='io.token.proto.common.providerspecific.ProviderTransactionDetails.details',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=368,
  serialized_end=528,
)


_PROVIDERTRANSFERMETADATA = _descriptor.Descriptor(
  name='ProviderTransferMetadata',
  full_name='io.token.proto.common.providerspecific.ProviderTransferMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='polish_api_transfer_metadata', full_name='io.token.proto.common.providerspecific.ProviderTransferMetadata.polish_api_transfer_metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
    _descriptor.OneofDescriptor(
      name='metadata', full_name='io.token.proto.common.providerspecific.ProviderTransferMetadata.metadata',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=531,
  serialized_end=686,
)


_CMA9ACCOUNTDETAILS_CMA9ADDRESS = _descriptor.Descriptor(
  name='Cma9Address',
  full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.Cma9Address',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address_type', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.Cma9Address.address_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.Cma9Address.address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1214,
  serialized_end=1378,
)

_CMA9ACCOUNTDETAILS = _descriptor.Descriptor(
  name='Cma9AccountDetails',
  full_name='io.token.proto.common.providerspecific.Cma9AccountDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='party_id', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.party_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='party_number', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.party_number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='party_type', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.party_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email_address', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.email_address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='phone', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.phone', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.mobile', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.address', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_type', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.account_type', index=8,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='account_subtype', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.account_subtype', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='io.token.proto.common.providerspecific.Cma9AccountDetails.description', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_CMA9ACCOUNTDETAILS_CMA9ADDRESS, ],
  enum_types=[
    _CMA9ACCOUNTDETAILS_PARTYTYPE,
    _CMA9ACCOUNTDETAILS_ADDRESSTYPE,
    _CMA9ACCOUNTDETAILS_ACCOUNTTYPE,
    _CMA9ACCOUNTDETAILS_ACCOUNTSUBTYPE,
  ],
  serialized_options=_b('\200\265\030\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=689,
  serialized_end=1870,
)

_PROVIDERACCOUNTDETAILS.fields_by_name['cma9_account_details'].message_type = _CMA9ACCOUNTDETAILS
_PROVIDERACCOUNTDETAILS.fields_by_name['polish_api_account_details'].message_type = polishapi__pb2._POLISHAPIACCOUNTDETAILS
_PROVIDERACCOUNTDETAILS.oneofs_by_name['details'].fields.append(
  _PROVIDERACCOUNTDETAILS.fields_by_name['cma9_account_details'])
_PROVIDERACCOUNTDETAILS.fields_by_name['cma9_account_details'].containing_oneof = _PROVIDERACCOUNTDETAILS.oneofs_by_name['details']
_PROVIDERACCOUNTDETAILS.oneofs_by_name['details'].fields.append(
  _PROVIDERACCOUNTDETAILS.fields_by_name['polish_api_account_details'])
_PROVIDERACCOUNTDETAILS.fields_by_name['polish_api_account_details'].containing_oneof = _PROVIDERACCOUNTDETAILS.oneofs_by_name['details']
_PROVIDERTRANSACTIONDETAILS.fields_by_name['polish_api_transaction_details'].message_type = polishapi__pb2._POLISHAPITRANSACTIONDETAILS
_PROVIDERTRANSACTIONDETAILS.oneofs_by_name['details'].fields.append(
  _PROVIDERTRANSACTIONDETAILS.fields_by_name['polish_api_transaction_details'])
_PROVIDERTRANSACTIONDETAILS.fields_by_name['polish_api_transaction_details'].containing_oneof = _PROVIDERTRANSACTIONDETAILS.oneofs_by_name['details']
_PROVIDERTRANSFERMETADATA.fields_by_name['polish_api_transfer_metadata'].message_type = polishapi__pb2._POLISHAPITRANSFERMETADATA
_PROVIDERTRANSFERMETADATA.oneofs_by_name['metadata'].fields.append(
  _PROVIDERTRANSFERMETADATA.fields_by_name['polish_api_transfer_metadata'])
_PROVIDERTRANSFERMETADATA.fields_by_name['polish_api_transfer_metadata'].containing_oneof = _PROVIDERTRANSFERMETADATA.oneofs_by_name['metadata']
_CMA9ACCOUNTDETAILS_CMA9ADDRESS.fields_by_name['address_type'].enum_type = _CMA9ACCOUNTDETAILS_ADDRESSTYPE
_CMA9ACCOUNTDETAILS_CMA9ADDRESS.fields_by_name['address'].message_type = address__pb2._ADDRESS
_CMA9ACCOUNTDETAILS_CMA9ADDRESS.containing_type = _CMA9ACCOUNTDETAILS
_CMA9ACCOUNTDETAILS.fields_by_name['party_type'].enum_type = _CMA9ACCOUNTDETAILS_PARTYTYPE
_CMA9ACCOUNTDETAILS.fields_by_name['address'].message_type = _CMA9ACCOUNTDETAILS_CMA9ADDRESS
_CMA9ACCOUNTDETAILS.fields_by_name['account_type'].enum_type = _CMA9ACCOUNTDETAILS_ACCOUNTTYPE
_CMA9ACCOUNTDETAILS.fields_by_name['account_subtype'].enum_type = _CMA9ACCOUNTDETAILS_ACCOUNTSUBTYPE
_CMA9ACCOUNTDETAILS_PARTYTYPE.containing_type = _CMA9ACCOUNTDETAILS
_CMA9ACCOUNTDETAILS_ADDRESSTYPE.containing_type = _CMA9ACCOUNTDETAILS
_CMA9ACCOUNTDETAILS_ACCOUNTTYPE.containing_type = _CMA9ACCOUNTDETAILS
_CMA9ACCOUNTDETAILS_ACCOUNTSUBTYPE.containing_type = _CMA9ACCOUNTDETAILS
DESCRIPTOR.message_types_by_name['ProviderAccountDetails'] = _PROVIDERACCOUNTDETAILS
DESCRIPTOR.message_types_by_name['ProviderTransactionDetails'] = _PROVIDERTRANSACTIONDETAILS
DESCRIPTOR.message_types_by_name['ProviderTransferMetadata'] = _PROVIDERTRANSFERMETADATA
DESCRIPTOR.message_types_by_name['Cma9AccountDetails'] = _CMA9ACCOUNTDETAILS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProviderAccountDetails = _reflection.GeneratedProtocolMessageType('ProviderAccountDetails', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDERACCOUNTDETAILS,
  '__module__' : 'providerspecific_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.providerspecific.ProviderAccountDetails)
  })
_sym_db.RegisterMessage(ProviderAccountDetails)

ProviderTransactionDetails = _reflection.GeneratedProtocolMessageType('ProviderTransactionDetails', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDERTRANSACTIONDETAILS,
  '__module__' : 'providerspecific_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.providerspecific.ProviderTransactionDetails)
  })
_sym_db.RegisterMessage(ProviderTransactionDetails)

ProviderTransferMetadata = _reflection.GeneratedProtocolMessageType('ProviderTransferMetadata', (_message.Message,), {
  'DESCRIPTOR' : _PROVIDERTRANSFERMETADATA,
  '__module__' : 'providerspecific_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.providerspecific.ProviderTransferMetadata)
  })
_sym_db.RegisterMessage(ProviderTransferMetadata)

Cma9AccountDetails = _reflection.GeneratedProtocolMessageType('Cma9AccountDetails', (_message.Message,), {

  'Cma9Address' : _reflection.GeneratedProtocolMessageType('Cma9Address', (_message.Message,), {
    'DESCRIPTOR' : _CMA9ACCOUNTDETAILS_CMA9ADDRESS,
    '__module__' : 'providerspecific_pb2'
    # @@protoc_insertion_point(class_scope:io.token.proto.common.providerspecific.Cma9AccountDetails.Cma9Address)
    })
  ,
  'DESCRIPTOR' : _CMA9ACCOUNTDETAILS,
  '__module__' : 'providerspecific_pb2'
  # @@protoc_insertion_point(class_scope:io.token.proto.common.providerspecific.Cma9AccountDetails)
  })
_sym_db.RegisterMessage(Cma9AccountDetails)
_sym_db.RegisterMessage(Cma9AccountDetails.Cma9Address)


DESCRIPTOR._options = None
_CMA9ACCOUNTDETAILS._options = None
# @@protoc_insertion_point(module_scope)
