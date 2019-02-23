# -*- coding: utf-8 -*-
import grpc

from tokenio.proto.gateway.gateway_pb2_grpc import GatewayServiceStub
from tokenio.rpc.interceptor.metadata_interceptor import MetadataInterceptor


class Channel:
    def __init__(self, rpc_uri, use_ssl, *interceptors):
        self.rpc_uri = rpc_uri
        self._channel = None
        self.use_ssl = use_ssl
        self.interceptors = interceptors

    @property
    def stub(self):
        if self.use_ssl:
            credentials = grpc.ssl_channel_credentials()
            self._channel = grpc.secure_channel(self.rpc_uri, credentials)
        else:
            self._channel = grpc.insecure_channel(self.rpc_uri)
        intercept_channel = grpc.intercept_channel(self._channel, *self.interceptors)
        stub = GatewayServiceStub(intercept_channel)
        return stub

    @classmethod
    def channel_factory(cls, rpc_uri='api-grpc.sandbox.token.io:443',
                        dev_key='4qY7lqQw8NOl9gng0ZHgT4xdiDqxqoGVutuZwrUYQsI', use_ssl=True):
        def create_channel_with_interceptors(*interceptors):
            metadata_interceptor = MetadataInterceptor({
                'token-sdk': 'python',
                'token-sdk-version': '0.0.1',
                'token-dev-key': dev_key
            })
            return cls(rpc_uri, use_ssl, metadata_interceptor, *interceptors)

        return create_channel_with_interceptors

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # TODO: Error Handle
        self._channel.close()
        return False
