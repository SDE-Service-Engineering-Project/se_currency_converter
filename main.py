from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from controller.conversion import EchoService, CurrencyConversionService
from services.conversion import convert_currency

app = Application([CurrencyConversionService, EchoService], 'http://localhost:8000/',
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(app)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()