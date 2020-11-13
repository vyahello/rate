from abc import ABC, abstractmethod
from rate.currencies import Currency, BRL, TJS, RUB, BYN, AUD, USD, EUR, PLN


class Injection(ABC):
    """Represent abstraction for currency injection."""

    @abstractmethod
    def perform(self) -> Currency:
        pass


class InjectionError(Exception):
    """Represent specific injection error object."""

    pass


class CurrencyInjection(Injection):
    """Inject concrete currency."""

    def __init__(self, currency: str) -> None:
        self._currency = currency

    def perform(self) -> Currency:
        if self._currency == "brl":
            return BRL()
        elif self._currency == "tjs":
            return TJS()
        elif self._currency == "rub":
            return RUB()
        elif self._currency == "byn":
            return BYN()
        elif self._currency == "aud":
            return AUD()
        elif self._currency == "usd":
            return USD()
        elif self._currency == "eur":
            return EUR()
        elif self._currency == "pln":
            return PLN()
        raise InjectionError("Invalid {} currency".format(self._currency))
