from abc import ABC, abstractmethod
from typing import Dict, Any
from rate.connections.requests import SafeGetRequest
from rate.connections.urls import HttpsUrl
from rate.currencies import Inject
from rate.dates import Date
from rate.logger import logger

_log = logger()


class Rate(ABC):
    """Represent abstraction for a specific rate."""

    @abstractmethod
    def value(self) -> None:
        pass


class ToUahRate(Rate):
    """Represent concrete specific currency exchange rate to `uah` currency.
    Current date will be as a default value."""

    def __init__(self, inject_currency: Inject, date: Date) -> None:
        def rate() -> Dict[Any, Any]:
            return SafeGetRequest(HttpsUrl('bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=',
                                           inject_currency.perform(), '&date=', date.date(),
                                           '&json')).response().as_dict()[0]

        self._rate = rate

    def value(self) -> None:
        _log.info('Exchange rate for UAH/%s is %s on %s', self._rate()['cc'], self._rate()['rate'],
                  self._rate()['exchangedate'])
