from spyne import Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication

from controller.currency import CurrencyConversionService

app = Application([CurrencyConversionService], tns="ccs",
                  name="CurrencyConversionService",
                  in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    wsgi_app = WsgiApplication(app)
    server = make_server('0.0.0.0', 8000, wsgi_app)
    server.serve_forever()
