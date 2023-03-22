from generated.currency_service_pb2 import ConversionResponse, CurrencyResponse, Currency
from generated.currency_service_pb2_grpc import CurrencyConversionServicer
from services.currency import convert_currency, list_all_currencies


class Converter(CurrencyConversionServicer):
    def Convert(self, request, context):
        converted_amount = convert_currency(request.amount, request.from_currency, request.to_currency)
        return ConversionResponse(amount=converted_amount)

    def GetCurrencies(self, request, context):
        return CurrencyResponse(currencies=[Currency(name=currency) for currency in list_all_currencies()])
