from abc import abstractmethod, ABC
import requests
import urllib3
from rate.connections.responses import Response, HttpResponse
from rate.connections.urls import Url


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class Session(ABC):
    """The abstraction of an API session."""

    @abstractmethod
    def get(self) -> Response:
        """Send a GET request."""
        pass


class ApiSession(Session):
    """Represent standard API session."""

    def __init__(self, url: Url, session: requests.Session = requests.Session()) -> None:
        self._session = session
        self._url = url

    def get(self) -> Response:
        return HttpResponse(self._session.get(self._url.compose(), verify=False))
