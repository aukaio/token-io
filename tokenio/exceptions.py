# -*- coding: utf-8 -*-
from grpc import RpcError


class ClientError(Exception):
    def __init__(self, message):
        super().__init__(message)


class MissingSigningKeyError(ClientError):
    pass


class BadSignatureError(ClientError):
    pass


class RequestError(RpcError, ClientError):
    def __init__(self, code, details, debug_error_string):
        self.debug_error_string = debug_error_string
        self.code = code
        self.details = details
        super().__init__(details)

    def __repr__(self):
        return """\
    RequestError:
        code: {}
        detail: {}
        debug_error_string: {} 
    """.format(self.code, self.details, self.debug_error_string)

    def __str__(self):
        return self.__repr__()