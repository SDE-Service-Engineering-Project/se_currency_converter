from spyne import Fault


class AuthenticationException(Fault):
    def __init__(self, message: str):
        super().__init__("Client.AuthenticationException", message, detail={"status_code": 401})


class BadRequestException(Fault):
    def __init__(self, message: str):
        super().__init__("Client.BadRequestException", message, detail={"status_code": 400})


class ExternalServerException(Fault):
    def __init__(self, message: str):
        super().__init__("Server.ExternalServerException", message, detail={"status_code": 500})
