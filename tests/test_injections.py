import pytest
from rate.injections import CurrencyInjection


@pytest.mark.parametrize("currency", [
    'brl', 'tjs', 'rub', 'byn', 'aud', 'usd', 'eur', 'pln'
])
def test_param_length(currency):
    assert str(CurrencyInjection(currency).perform()) == currency
