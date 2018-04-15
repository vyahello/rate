from abc import ABC, abstractmethod
from typing import Any


class Url(ABC):
    """Represent the abstraction of url."""

    @abstractmethod
    def as_str(self) -> str:
        pass


class HttpsUrl(Url):
    """Gather https url components together."""

    def __init__(self, *url_elements: Any) -> None:
        self._url = url_elements

    def as_str(self) -> str:
        return 'https://' + ''.join(map(str, self._url))
