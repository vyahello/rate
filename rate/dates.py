from abc import ABC, abstractmethod
import re


class Date(ABC):
    """Represent abstraction for a date."""

    @abstractmethod
    def get(self) -> str:
        pass


class DateError(Exception):
    """Represent date error object."""

    pass


class SafeDate(Date):
    """Represent safe date object."""

    def __init__(self, value: str) -> None:
        self._value = value

    def get(self) -> str:
        if not re.compile('\d{4}-\d{2}-\d{2}').findall(self._value):
            raise DateError("Incorrect date format. Date has to be in YYYY-MM-DD format.")
        return self._value


class CustomDate(Date):
    """Represent specific for a date."""

    def __init__(self, value: str) -> None:
        self._date: Date = SafeDate(value)

    def get(self) -> str:
        return ''.join(map(lambda i: str(i), re.split('-', self._date.get())))
