# -*- coding: utf-8 -*-
import typing

import tokenio.member
from tokenio import utils
from tokenio.exceptions import IllegalArgumentException
from tokenio.token_request import TokenRequest, TokenRequestState
from tokenio.proto.account_pb2 import BankAccount
from tokenio.proto.alias_pb2 import Alias
from tokenio.proto.blob_pb2 import Blob
from tokenio.proto.pricing_pb2 import Pricing
from tokenio.proto.token_pb2 import TokenRequestPayload, TokenMember, ActingAs
from tokenio.proto.transferinstructions_pb2 import TransferInstructions, TransferEndpoint, TransferDestination
TransferBody = TokenRequestPayload.TransferBody

class TransferTokenBuilder:
    def __init__(
        self, member: 'tokenio.member.Member',
        amount: typing.Union[str, float], currency: str
    ) -> None:
        self.member = member
        self.amount = amount
        self.currency = currency
        self.request_state = TokenRequestState('', '')

        transfer_body = TransferBody(
            currency=currency,
            lifetime_amount=str(amount),
            instructions=TransferInstructions(
                source=TransferEndpoint(),
                metadata=TransferInstructions.Metadata()
            )
        )
        self.payload = TokenRequestPayload(
            to=TokenMember(),
            transfer_body=transfer_body
        )

        self.blob_payloads = []

    def set_account_id(self, account_id: str) -> 'TransferTokenBuilder':
        token = BankAccount.Token(
            account_id=account_id, member_id=self.member.member_id
        )
        source_account = BankAccount(token=token)

        self.payload.transfer_body.instructions.source.account.CopyFrom(
            source_account
        )
        return self

    def set_custom_authorization(
        self, bank_id: str, authorization: str
    ) -> 'TransferTokenBuilder':
        custom = BankAccount.Custom(bank_id=bank_id, payload=authorization)
        source_account = BankAccount(custom=custom)
        self.payload.transfer_body.instructions.source.account.CopyFrom(
            source_account
        )
        return self

    def set_expires_at_ms(self, expires_at_ms: int) -> 'TransferTokenBuilder':
        self.payload.expires_at_ms = expires_at_ms
        return self

    def set_effective_at_ms(
        self, effective_at_ms: int
    ) -> 'TransferTokenBuilder':
        self.payload.effective_at_ms = effective_at_ms
        return self

    def set_endorse_until_ms(
        self, endorse_until_ms: int
    ) -> 'TransferTokenBuilder':
        self.payload.endorse_until_ms = endorse_until_ms
        return self

    def set_change_amount(
        self, charge_amount: typing.Union[str, float]
    ) -> 'TransferTokenBuilder':
        self.payload.transfer_body.amount = str(charge_amount)
        return self

    def set_description(self, description: str) -> 'TransferTokenBuilder':
        self.payload.description = description
        return self

    def set_source(self, source: TransferEndpoint) -> 'TransferTokenBuilder':
        self.payload.transfer_body.instructions.source.CopyFrom(source)
        return self

    def add_destination(
        self, destination: TransferDestination
    ) -> 'TransferTokenBuilder':
        self.payload.transfer_body.instructions.transfer_destinations.extend([destination])
        return self

    # def add_attachment(
    #     self, attachment: Attachment
    # ) -> 'TransferTokenBuilder':
    #     self.payload.transfer_body.attachments.extend([attachment])
    #     return self

    # def add_attachment_by_filename(
    #     self, owner_id: str, file_type: str, file_name: str, data: bytes
    # ) -> 'TransferTokenBuilder':
    #     payload = Blob.Payload(
    #         owner_id=owner_id, type=file_type, name=file_name, data=data
    #     )
    #     self.blob_payloads.append(payload)
    #     return self

    def set_to_alias(self, to_alias: Alias) -> 'TransferTokenBuilder':
        self.payload.to.alias.CopyFrom(to_alias)
        return self

    def set_to_member_id(self, member_id: str) -> 'TransferTokenBuilder':
        self.payload.to.id = member_id
        return self

    def set_ref_id(self, ref_id: str) -> 'TransferTokenBuilder':
        ref_id_length = len(ref_id)
        if ref_id_length > 18:
            raise IllegalArgumentException(
                'The length of the ref_id is at most 18, got: {}'.
                format(ref_id_length)
            )
        self.payload.ref_id = ref_id
        return self

    def set_pricing(self, pricing: Pricing) -> 'TransferTokenBuilder':
        self.payload.transfer_body.pricing.CopyFrom(pricing)
        return self

    def set_purpose_of_payment(
        self, purpose_of_payment: int
    ) -> 'TransferTokenBuilder':
        self.payload.transfer_body.instructions.metadata.transfer_purpose = purpose_of_payment
        return self

    def set_acting_as(self, acting_as: ActingAs) -> 'TransferTokenBuilder':
        self.payload.acting_as.CopyFrom(acting_as)
        return self

    def set_redirect_url(self, redirect_url):
        self.payload.redirect_url = redirect_url
        return self

    def set_state(self, state):
        self.request_state.state = state
        return self

    def set_csrf_token(self, token):
        self.request_state.csrf_token_hash = utils.hash_string(token)
        return self

    def build(self) -> TokenRequestPayload:
        to = self.payload.to
        if len(to.id) == 0 and to.alias.ByteSize() == 0:
            raise IllegalArgumentException('No payee on token request')
        self.payload.callback_state = self.request_state.serialize()
        return self.payload

    def build_with_blob_attachments(self) -> TokenRequestPayload:
        self.build()

        redeemer = self.payload.to
        if len(redeemer.id) == 0 and redeemer.alias.ByteSize() == 0:
            raise IllegalArgumentException('No redeemer on token')

        if len(self.payload.ref_id) == 0:
            self.payload.ref_id = utils.generate_nonce()

        attachment_uploads = []
        for blob_payload in self.blob_payloads:
            attachment = self.member.create_blob(
                blob_payload.owner_id, blob_payload.type, blob_payload.name,
                blob_payload.data
            )
            if attachment.ByteSize() != 0:
                attachment_uploads.append(attachment)

        self.payload.transfer_body.attachments.extend(attachment_uploads)
        return self
