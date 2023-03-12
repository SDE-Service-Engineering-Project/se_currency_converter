from functools import lru_cache

import jwt
from jwt import InvalidSignatureError, ExpiredSignatureError
from spyne import ComplexModel, Unicode

from exceptions.exceptions import AuthenticationException


class AuthenticationHeader(ComplexModel):
    __namespace__ = "ccs"
    __type_name__ = "credentials"
    _type_info = [
        ('token', Unicode.customize(min_occurs=1, nillable=False)),
    ]


def authenticate(ctx):
    if ctx.in_header is None:
        raise AuthenticationException("Authentication header is not present")
    try:
        token = ctx.in_header.token
        pub_key = load_pub_key()
        jwt.decode(token, pub_key, algorithms=["RS256"])
    except InvalidSignatureError:
        raise AuthenticationException("Authentication failed")
    except ExpiredSignatureError:
        raise AuthenticationException("Token expired")


@lru_cache(maxsize=1)
def load_pub_key():
    with open('resources/key.pub') as f:
        pub_key = f.read()
    return pub_key
