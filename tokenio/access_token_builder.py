# -*- coding: utf-8 -*-
from tokenio import utils
from tokenio.exceptions import IllegalArgumentException
from tokenio.proto.alias_pb2 import Alias
from tokenio.proto.token_pb2 import TokenRequestPayload, TokenMember

AccessBody = TokenRequestPayload.AccessBody

class AccessTokenBuilder:
    def __init__(self, payload=None):
        self.payload = payload
        if payload is None:
            self.payload = TokenRequestPayload(
                ref_id=utils.generate_nonce(),
                access_body=AccessBody(),
                to=TokenMember()
            )

    @classmethod
    def create_with_alias(cls, redeemer_alias: Alias):
        return cls().alias_to(redeemer_alias)

    @classmethod
    def create_with_redeemer_id(cls, redeemer_member_id: str):
        return cls().redeemer_to(redeemer_member_id)

    def alias_to(self, redeemer_alias):
        self.payload.to.alias.CopyFrom(redeemer_alias)
        return self

    def redeemer_to(self, redeemer_member_id: str):
        self.payload.to.alias.id = redeemer_member_id
        return self

    @classmethod
    def from_payload(cls, payload: TokenRequestPayload):
        new_payload = TokenRequestPayload()
        new_payload.CopyFrom(payload)
        new_payload.access.CopyFrom(AccessBody())
        new_payload.ref_id = utils.generate_nonce()
        return cls(new_payload)

    def for_all(self):
        return self.for_all_accounts(). \
            for_all_balances(). \
            for_all_transactions(). \
            for_all_transfer_destinations()

    def for_all_accounts(self):
        self.__add_resource(AccessBody.ACCOUNTS)
        return self

    def for_all_transactions(self):
        self.__add_resource(AccessBody.TRANSACTIONS)
        return self

    def for_all_balances(self):
        self.__add_resource(AccessBody.BALANCES)
        return self

    def for_all_transfer_destinations(self):
        self.__add_resource(AccessBody.TRANSFER_DESTINATIONS)
        return self

    def __add_resource(self, resource):
        self.payload.access_body.type.extend([resource])
        return self

    def build(self):
        if len(self.payload.access_body.type) == 0:
            raise IllegalArgumentException(
                'At least one access resource must be set'
            )
        return self.payload
