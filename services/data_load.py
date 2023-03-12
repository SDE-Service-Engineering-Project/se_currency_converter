from datetime import date
from functools import lru_cache

import requests
import xmltodict

from exceptions.exceptions import ExternalServerException


@lru_cache(maxsize=1)
def load_currencies(input_date: date) -> dict:
    """ The input parameter only functions as a cache key. The actual date is parsed from the response."""
    try:
        response = requests.get('https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml')
    except Exception as e:
        raise ExternalServerException(f"The external server hosting the currencies could not be reached: {e}")
    if response.status_code != 200:
        raise ExternalServerException(f"The external server hosting the currencies could not be reached.")

    try:
        data = xmltodict.parse(response.text)
        currency_entries = data['gesmes:Envelope']['Cube']['Cube']['Cube']
    except Exception as e:
        raise ExternalServerException(f"The response of the external service is malformed: {e}")
    currency_dict = dict([(item['@currency'], float(item['@rate'])) for item in currency_entries])
    currency_dict['EUR'] = 1.0

    return currency_dict
