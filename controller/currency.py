from spyne import rpc, ServiceBase, Unicode, Float, Array

from services.auth import authenticate, AuthenticationHeader
from services.currency import convert_currency, list_all_currencies


class CurrencyConversionService(ServiceBase):
    __tns__ = 'ccs'
    __in_header__ = AuthenticationHeader

    @rpc(Float.customize(min_occurs=1, nillable=False), Unicode.customize(min_occurs=1, nillable=False),
         Unicode.customize(min_occurs=1, nillable=False), _returns=Float)
    def convert(self, amount, from_currency, to_currency):
        return convert_currency(amount, from_currency, to_currency)

    @rpc(_returns=Array(Unicode))
    def list_currencies(self):
        return list_all_currencies()


CurrencyConversionService.event_manager.add_listener('method_call', authenticate)
