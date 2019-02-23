# -*- coding: utf-8 -*-
class TokenIOError(Exception):
    def __init__(self, message):
        super().__init__(message)


class MissingSigningKeyError(TokenIOError):
    pass


class BadSignatureError(TokenIOError):
    pass
