from datetime import date
from functools import lru_cache

import requests
import xmltodict
from spyne.error import InternalError


@lru_cache(maxsize=1)
def load_currencies(input_date: date) -> dict:
    """ The input parameter only functions as a cache key. The actual date is parsed from the response."""
    try:
        response = requests.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')
    except Exception as e:
        raise InternalError(f"The external server hosting the currencies could not be reached: {e}")

    try:
        data = xmltodict.parse(response.text)
        currency_entries = data['gesmes:Envelope']['Cube']['Cube']['Cube']
    except Exception as e:
        raise InternalError(f"The response of the external is malformatted: {e}")
    currency_dict = dict([(item['@currency'], float(item['@rate'])) for item in currency_entries])

    return currency_dict
