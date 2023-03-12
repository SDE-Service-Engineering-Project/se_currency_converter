import pytest

from exceptions.exceptions import AuthenticationException
from services.auth import authenticate


class MockInHeader:
    def __init__(self, token):
        self.token = token


class MockContext:
    def __init__(self, in_header):
        self.in_header = in_header


def test_authenticate_token_expired():
    # Arrange
    token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzZWxmIiwic3ViIjoic2FoaWwiLCJleHAiOjE2Nzg2MjMxOTMsImlhdCI6MTY3ODYyMzA3Mywic2NvcGUiOiJST0xFX1VTRVIifQ.oCDjroI1np51FyAjBOtflEyy63moxlFrOI31omU2qtTSxMHjm-d7MV-UP-cTYVj3zJYxzIG-cLTX_ePEhQVDvQFOYX8UCuirdGogqW9E-JfH7FiRmgtT4-eYry-L0WuWwhTa6EVjlQ-7S4XHoGAIZO-1KqKaV_9jEJv5W03dwchgn9efN1hCUF2o06EiKzPKp0idvy5Bw6Drg7cdNQ34XOlLhPXySyfrO9fr7fxYA93Q7LlUq_3PHk9OX27FV39RHIg-ejHldgh7NoJjqyAa6w7zZUc0-u934tQQfNZqpx_ljdMO9oNkuVz8iTBoAIA-Tnwvgyjvi7br3JJ-TYxg7A"
    ctx = MockContext(in_header=MockInHeader(token))

    with pytest.raises(AuthenticationException):
        authenticate(ctx)


def test_authenticate_invalid_signature():
    # Arrange
    token = "eyJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJzZWxmIiwic3ViIjoic2FoaWwiLCJleHAiOjE2Nzg2MjMxOTMsImlhdCI6MTY3ODYyMzA3Mywic2NvcGUiOiJST0xFX1VTRVIifQ.oCDjroI1np51FyAjBOtflEyy63moxlFrOI31omU2qtTSxMHjm-d7MV-UP-cTYVj3zJYxzIG-cLTX_ePEhQVDvQFOYX8UCuirdGogqW9E-JfH7FiRmgtT4-eYry-L0WuWwhTa6EVjlQ-7S4XHoGAIZO-1KqKaV_9jEJv5W03dwchgn9efN1hCUF2o06EiKzPKp0idvy5Bw6Drg7cdNQ34XOlLhPXySyfrO9fr7fxYA93Q7LlUq_3PHk9OX27FV39RHIg-ejHldgh7NoJjqyAa6w7zZUc0-u934tQQfNZqpx_ljdMO9oNkuVz8iTBoAIA-Tnwvgyjvi7br3JG-TYxg7A"
    ctx = MockContext(in_header=MockInHeader(token))
    # Act & Assert
    with pytest.raises(AuthenticationException):
        authenticate(ctx)
