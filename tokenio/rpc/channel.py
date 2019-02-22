# -*- coding: utf-8 -*-
import grpc

from tokenio.proto.gateway.gateway_pb2_grpc import GatewayServiceStub
from tokenio.rpc.client_authenticator_interceptor import ClientAuthenticatorInterceptor


class BaseChannel:
    def __init__(self, rpc_url='api-grpc.sandbox.token.io:443'):
        self.rpc_url = rpc_url
        self.credentials = grpc.ssl_channel_credentials()
        self._channel = None

    @property
    def stub(self):
        self._channel = grpc.secure_channel(self.rpc_url, self.credentials)
        stub = GatewayServiceStub(self._channel)
        return stub

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Error Handle
        self._channel.close()
        return False


class UnauthenticatedChannel(BaseChannel):
    pass


class Channel(BaseChannel):
    def __init__(self, member_id, crypto_engine, rpc_url='api-grpc.sandbox.token.io:443'):
        super().__init__(rpc_url)
        self.member_id = member_id
        self.crypto_engine = crypto_engine
        self.credentials = grpc.ssl_channel_credentials()
        self._channel = None

    @property
    def stub(self):
        interceptor = ClientAuthenticatorInterceptor(member_id=self.member_id, crypto_engine=self.crypto_engine)
        self._channel = grpc.secure_channel(self.rpc_url, self.credentials)
        intercept_channel = grpc.intercept_channel(self._channel, interceptor)
        stub = GatewayServiceStub(intercept_channel)
        return stub
