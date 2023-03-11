from spyne import rpc, ServiceBase, Unicode, Float

from models.auth import _authenticate, AuthenticationHeader
from services.conversion import convert_currency


class CurrencyConversionService(ServiceBase):
    __tns__ = 'ccs'
    __in_header__ = AuthenticationHeader

    @rpc(Float.customize(min_occurs=1, nillable=False), Unicode.customize(min_occurs=1, nillable=False),
         Unicode.customize(min_occurs=1, nillable=False), _returns=Float)
    def convert(ctx, amount, from_currency, to_currency):
        return convert_currency(amount, from_currency, to_currency)


CurrencyConversionService.event_manager.add_listener('method_call', _authenticate)
