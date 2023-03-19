import pytest

from exceptions.exceptions import BadRequestException
from services.currency import convert_currency, ensure_currencies_are_supported

mocked_currency_conversion_rates = {'EUR': 1.0, 'USD': 1.1}


def test_convert_currency_single_convert_success(mocker):
    # Arrange
    mocker.patch('services.conversion.load_currencies', return_value=mocked_currency_conversion_rates)
    # Act & Assert
    assert convert_currency(2.0, 'EUR', 'USD') == 2.2


def test_convert_currency_multiple_convert_success(mocker):
    # Arrange
    original_input = 2.0
    mocker.patch('services.conversion.load_currencies', return_value=mocked_currency_conversion_rates)
    # Act
    first_call_result = convert_currency(original_input, 'EUR', 'USD')
    second_call_result = convert_currency(first_call_result, 'USD', 'EUR')
    # Assert
    assert second_call_result == original_input


def test_ensure_currencies_are_supported_success():
    # Arrange
    conversion_rates = mocked_currency_conversion_rates
    # Act & Assert
    try:
        ensure_currencies_are_supported(conversion_rates, ('EUR', 'USD'))
    except BadRequestException:
        # Assert
        assert False


def test_ensure_currencies_are_supported_fail():
    # Arrange
    conversion_rates = mocked_currency_conversion_rates
    # Act 6 Assert
    with pytest.raises(BadRequestException):
        ensure_currencies_are_supported(conversion_rates, ('SEK', 'USD'))
