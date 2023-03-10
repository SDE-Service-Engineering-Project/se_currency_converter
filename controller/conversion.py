from spyne import rpc, ServiceBase, Unicode, Float, String

from services.conversion import convert_currency


class EchoService(ServiceBase):
    @rpc(Unicode, _returns=Unicode)
    def echo(ctx, text):
        return text


class CurrencyConversionService(ServiceBase):
    @rpc(Float, String, _returns=Float)
    def convert(ctx, amount, to_currency):
        return convert_currency(amount, to_currency)
