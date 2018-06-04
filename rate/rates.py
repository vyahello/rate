import logging
from abc import ABC, abstractmethod
from rate.connections.requests import Get
from rate.connections.urls import UnifiedUrl
from rate.injections import Injection
from rate.dates import Date
from rate.logger import logger

_log: logging.Logger = logger()
_url: str = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={c}&date={d}&json'


class Rate(ABC):
    """Represent abstraction for a specific rate."""

    @abstractmethod
    def value(self) -> None:
        pass


class ToUahRate(Rate):
    """Represent concrete specific currency exchange rate to `uah` currency.
    Current date will be as a default value."""

    def __init__(self, inject: Injection, date: Date) -> None:
        self._date = date
        self._inj_cur = inject

    def value(self) -> None:
        data = Get(UnifiedUrl(_url.format(c=self._inj_cur.perform(), d=self._date.get()))).response().as_dict()[0]
        _log.info('Exchange rate for UAH/%s is %s on %s', data['cc'], data['rate'], data['exchangedate'])
