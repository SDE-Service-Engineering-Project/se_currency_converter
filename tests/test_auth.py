import unittest.mock as mock

import pytest
from grpc import ServicerContext
from grpc_interceptor.exceptions import Unauthenticated

from controller.currency import Converter
from services.auth import JWTAuthInterceptor, load_pub_key

interceptor = JWTAuthInterceptor(load_pub_key())


def test_authenticate_token_expired():
    # Arrange
    token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzZWxmIiwic3ViIjoic2FoaWwiLCJleHAiOjE2Nzg2MjMxOTMsImlhdCI6MTY3ODYyMzA3Mywic2NvcGUiOiJST0xFX1VTRVIifQ.oCDjroI1np51FyAjBOtflEyy63moxlFrOI31omU2qtTSxMHjm-d7MV-UP-cTYVj3zJYxzIG-cLTX_ePEhQVDvQFOYX8UCuirdGogqW9E-JfH7FiRmgtT4-eYry-L0WuWwhTa6EVjlQ-7S4XHoGAIZO-1KqKaV_9jEJv5W03dwchgn9efN1hCUF2o06EiKzPKp0idvy5Bw6Drg7cdNQ34XOlLhPXySyfrO9fr7fxYA93Q7LlUq_3PHk9OX27FV39RHIg-ejHldgh7NoJjqyAa6w7zZUc0-u934tQQfNZqpx_ljdMO9oNkuVz8iTBoAIA-Tnwvgyjvi7br3JJ-TYxg7A"
    context_stub = mock.create_autospec(ServicerContext)

    def return_invocation_metadata():
        return {'authorization': token}

    context_stub.invocation_metadata = return_invocation_metadata
    # Act
    with pytest.raises(Unauthenticated) as e_info:
        interceptor.intercept(Converter.Convert, None, context_stub, None)
    # Assert
    assert e_info.value.details == "The token has expired"


def test_authenticate_invalid_signature():
    # Arrange
    token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzZWxmIiwic3ViIjoic2FoaWwiLCJleHAiOjE2Nzg2MjMxOTMsImlhdCI6MTY3ODYyMzA3Mywic2NvcGUiOiJST0xFX1VTRVIifQ.oCDjroI1np51FyAjBOtflEyy63moxlFrOI31omU2qtTSxMHjm-d7MV-UP-cTYVj3zJYxzIG-cLTX_ePEhQVDvQFOYX8UCuirdGogqW9E-JfH7FiRmgtT4-eYry-L0WuWwhTa6EVjlQ-7S4XHoGAIZO-1KqKaV_9jEJv5W03dwchgn9efN1hCUF2o06EiKzPKp0idvy5Bw6Drg7cdNQ34XOlLhPXySyfrO9fr7fxYA93Q7LlUq_3PHk9OX27FV39RHIg-ejHldgh7NoJjqyAa6w7zZUc0-u934tQQfNZqpx_ljdMO9oNkuVz8iTBoAIA-Tnwvgyjvi7br3JG-TYxg7A"
    context_stub = mock.create_autospec(ServicerContext)

    def return_invocation_metadata():
        return {'authorization': token}

    context_stub.invocation_metadata = return_invocation_metadata

    # Act
    with pytest.raises(Unauthenticated) as e_info:
        interceptor.intercept(Converter.Convert, None, context_stub, None)
    # Assert
    assert e_info.value.details == "The token signature is invalid"


def test_authenticate_invalid_token():
    # Arrange
    token = "asdf"
    context_stub = mock.create_autospec(ServicerContext)

    def return_invocation_metadata():
        return {'authorization': token}

    context_stub.invocation_metadata = return_invocation_metadata

    with pytest.raises(Unauthenticated) as e_info:
        interceptor.intercept(Converter.Convert, None, context_stub, None)
    assert e_info.value.details == "The token is not valid"
