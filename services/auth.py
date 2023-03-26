from functools import lru_cache
from typing import Callable, Any

import grpc
import jwt
from grpc_interceptor import ServerInterceptor
from grpc_interceptor.exceptions import GrpcException, Unauthenticated
from jwt import InvalidSignatureError, ExpiredSignatureError, DecodeError


class JWTAuthInterceptor(ServerInterceptor):
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def intercept(
            self,
            method: Callable,
            request: Any,
            context: grpc.ServicerContext,
            method_name: str,
    ) -> Any:
        try:
            metadata = dict(context.invocation_metadata())
            if 'authorization' not in metadata:
                raise Unauthenticated('Authentication header is not present', grpc.StatusCode.UNAUTHENTICATED)
            token = metadata['authorization']
            try:
                jwt.decode(token, self.secret_key, algorithms=['RS256'])
            except InvalidSignatureError:
                raise Unauthenticated('The token signature is invalid', grpc.StatusCode.UNAUTHENTICATED)
            except ExpiredSignatureError:
                raise Unauthenticated('The token has expired', grpc.StatusCode.UNAUTHENTICATED)
            except DecodeError:
                raise Unauthenticated('The token is not valid', grpc.StatusCode.UNAUTHENTICATED)
            return method(request, context)
        except GrpcException as e:
            context.set_code(e.status_code)
            context.set_details(e.details)
            raise


@lru_cache(maxsize=1)
def load_pub_key():
    with open('resources/key.pub') as f:
        pub_key = f.read()
    return pub_key
