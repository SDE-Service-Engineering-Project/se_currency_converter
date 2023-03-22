from datetime import date

from exceptions.exceptions import BadRequestException
from services.data_load import load_currencies


def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    exchange_rates = load_currencies()
    ensure_currencies_are_supported(exchange_rates, (to_currency, from_currency))
    return amount * (exchange_rates[to_currency] / exchange_rates[from_currency])


def list_all_currencies() -> list:
    exchange_rates = load_currencies()
    return list(exchange_rates.keys())


def ensure_currencies_are_supported(exchange_rates: dict, currencies: tuple):
    for currency in currencies:
        if currency not in exchange_rates:
            raise BadRequestException(f"Currency {currency} is not supported.")
