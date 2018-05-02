from abc import ABC, abstractmethod
from rate.connections.api import CustomApiSession, ApiSession
from rate.connections.responses import Response
from rate.connections.urls import Url


class Request(ABC):
    """The abstraction of a specific API request."""

    @abstractmethod
    def response(self) -> Response:
        pass


class RequestError(Exception):
    """Represent request error object."""

    pass


class GetRequest(Request):
    """Represent a GET request."""

    def __init__(self, url: Url) -> None:
        self._session: ApiSession = CustomApiSession(url)

    def response(self) -> Response:
        return self._session.get()


class SafeGetRequest(Request):
    """Represent a safe GET request.
    Raise error if `200` response status code is not presented.
    """

    def __init__(self, url: Url, status_code: int = 200) -> None:
        self._req: Request = GetRequest(url)
        self._code = status_code

    def response(self) -> Response:
        if self._req.response().status_code() != self._code:
            raise RequestError('HTTP request error with {} status code!!!'.format(self._req.response().status_code()))
        return self._req.response()
