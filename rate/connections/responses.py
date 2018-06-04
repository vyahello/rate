from abc import ABC, abstractmethod
from typing import Dict, Any
import requests


class Response(ABC):
    """The abstraction of a response from an api request."""

    @abstractmethod
    def as_dict(self) -> Dict[Any, Any]:
        pass


class HttpResponse(Response):
    """Represent an HTTP response from an api request."""

    def __init__(self, response: requests.Response) -> None:
        self._response = response

    def as_dict(self) -> Dict[Any, Any]:
        return self._response.json()
