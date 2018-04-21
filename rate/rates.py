from abc import ABC, abstractmethod
from rate.connections.requests import SafeGetRequest
from rate.connections.urls import HttpsUrl
from rate.injections import Injection
from rate.dates import Date
from rate.logger import logger

_log = logger()


class ExchangeRate(ABC):
    """Represent abstraction for a specific rate."""

    @abstractmethod
    def value(self) -> None:
        pass


class ToUahExchangeRate(ExchangeRate):
    """Represent concrete specific currency exchange rate to `uah` currency.
    Current date will be as a default value."""

    def __init__(self, inject_currency: Injection, date: Date) -> None:
        self._date = date
        self._inject_currency = inject_currency

    def value(self) -> None:
        data = SafeGetRequest(HttpsUrl('bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=',
                                       self._inject_currency.perform(), '&date=', self._date.date(),
                                       '&json')).response().as_dict()[0]
        _log.info('Exchange rate for UAH/%s is %s on %s', data['cc'], data['rate'], data['exchangedate'])
