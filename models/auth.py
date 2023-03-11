import hmac

import bcrypt
from spyne import ComplexModel, Unicode

from entity.db import Session, User
from exceptions.exceptions import AuthenticationException


class AuthenticationHeader(ComplexModel):
    __namespace__ = "ccs"
    __type_name__ = "credentials"
    _type_info = [
        ('username', Unicode.customize(min_occurs=1, nillable=False)),
        ('password', Unicode.customize(min_occurs=1, nillable=False))
    ]


def _authenticate(ctx):
    if ctx.in_header is None:
        raise AuthenticationException("Authentication header is not present")
    user = Session.get_instance().query(User).filter_by(username=ctx.in_header.username).first()

    if user is None:
        raise AuthenticationException("Authentication failed")
    hashed_password_input = bcrypt.hashpw(ctx.in_header.password.encode('utf-8'), user.salt)

    if not hmac.compare_digest(user.password, hashed_password_input): # Why not "=="? -> https://docs.python.org/3/library/hmac.html
        raise AuthenticationException("Authentication failed")
