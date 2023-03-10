from datetime import date

from spyne import Fault

from services.data_load import load_currencies


def convert_currency(amount: float, to_currency: str):
    exchange_rates = load_currencies(date.today())
    if to_currency not in exchange_rates:
        raise Fault("Client", f"Currency {to_currency} is not supported.")
    return amount * (exchange_rates[to_currency] / exchange_rates['USD'])
