from abc import ABC, abstractmethod
from rate.connections.api import ApiSession, Session
from rate.connections.responses import Response
from rate.connections.urls import Url


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def response(self) -> Response:
        pass


class Get(Request):
    """Represent a GET request."""

    def __init__(self, url: Url) -> None:
        self._session: Session = ApiSession(url)

    def response(self) -> Response:
        return self._session.get()
