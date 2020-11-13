from abc import ABC, ABCMeta, abstractmethod


class Currency(ABC):
    """Represent abstraction for a specific currency."""

    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self) -> str:
        pass


class BRL(Currency):
    """Represent `Brazil real` currency."""

    def __str__(self) -> str:
        return "brl"


class TJS(Currency):
    """Represent `Samoni` currency."""

    def __str__(self) -> str:
        return "tjs"


class RUB(Currency):
    """Represent `Russian ruble` currency."""

    def __str__(self) -> str:
        return "rub"


class RSD(Currency):
    """Represent `Serbian dinar` currency."""

    def __str__(self) -> str:
        return "rsd"


class BYN(Currency):
    """Represent `Belorussian ruble` currency."""

    def __str__(self) -> str:
        return "byn"


class AUD(Currency):
    """Represent `Australian dollar` currency."""

    def __str__(self) -> str:
        return "aud"


class USD(Currency):
    """Represent `American dollar` currency."""

    def __str__(self) -> str:
        return "usd"


class EUR(Currency):
    """Represent `EURO` currency."""

    def __str__(self) -> str:
        return "eur"


class PLN(Currency):
    """Represent `Polish Zloty` currency."""

    def __str__(self) -> str:
        return "pln"
