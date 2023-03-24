from datetime import date

import pytest
import requests_mock
from grpc_interceptor.exceptions import Unavailable

from services.data_load import load_currencies


def test_load_currencies_server_unavailable():
    with requests_mock.Mocker() as m:
        # Arrange
        m.get("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml", status_code=404)
        # Act & Assert
        with pytest.raises(Unavailable):
            load_currencies()


def test_load_currencies_malformed_content():
    with requests_mock.Mocker() as m:
        # Arrange
        m.get("https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml", status_code=200, text="malformed content")
        # Act & Assert
        with pytest.raises(Unavailable):
            load_currencies()

