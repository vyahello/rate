from abc import ABC, abstractmethod


class Currency(ABC):
    """Represent abstraction for a specific currency."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class Inject(ABC):
    """Represent abstraction for injection."""

    @abstractmethod
    def perform(self) -> Currency:
        pass


class CurrencyError(Exception):
    """Represent currency error."""

    pass


class InjectCurrency(Inject):
    """Inject concrete currency."""

    def __init__(self, currency: str):
        self._currency = currency

    def perform(self) -> Currency:
        if self._currency == 'brl':
            return BRL()
        elif self._currency == 'tjs':
            return TJS()
        elif self._currency == 'rub':
            return RUB()
        elif self._currency == 'byn':
            return BYN()
        elif self._currency == 'aud':
            return AUD()
        elif self._currency == 'usd':
            return USD()
        elif self._currency == 'eur':
            return EUR()
        elif self._currency == 'pln':
            return PLN()
        else:
            raise CurrencyError('Invalid {} currency'.format(self._currency))


class BRL(Currency):
    """Represent `Brazil real` currency."""

    def __str__(self) -> str:
        return 'brl'


class TJS(Currency):
    """Represent `Samoni` currency."""

    def __str__(self) -> str:
        return 'tjs'


class RUB(Currency):
    """Represent `Russian ruble` currency."""

    def __str__(self) -> str:
        return 'rub'


class RSD(Currency):
    """Represent `Serbian dinar` currency."""

    def __str__(self) -> str:
        return 'rsd'


class BYN(Currency):
    """Represent `Belorussian ruble` currency."""

    def __str__(self) -> str:
        return 'byn'


class AUD(Currency):
    """Represent `Australian dollar` currency."""

    def __str__(self) -> str:
        return 'aud'


class USD(Currency):
    """Represent `American dollar` currency."""

    def __str__(self) -> str:
        return 'usd'


class EUR(Currency):
    """Represent `EURO` currency."""

    def __str__(self) -> str:
        return 'eur'


class PLN(Currency):
    """Represent `Polish Zloty` currency."""

    def __str__(self) -> str:
        return 'pln'
