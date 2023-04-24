import logging

from generated.currency_service_pb2 import ConversionResponse, CurrencyResponse, Currency
from generated.currency_service_pb2_grpc import CurrencyConversionServicer
from services.currency import convert_currency, list_all_currencies

log = logging.getLogger("currency_converter")


class Converter(CurrencyConversionServicer):
    def convert(self, request, context):
        log.info(f"Converting {request.amount} {request.from_currency} to {request.to_currency}")
        converted_amount = convert_currency(request.amount, request.from_currency, request.to_currency)
        return ConversionResponse(amount=converted_amount)

    def getCurrencies(self, request, context):
        log.info("Retrieving all currencies")
        return CurrencyResponse(currencies=[Currency(name=currency) for currency in list_all_currencies()])
