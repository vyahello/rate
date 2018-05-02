from rate.connections.urls import HttpsUrl

_url: str = 'https://path/to/data&data'


def test_url() -> None:
    assert HttpsUrl('path/to/', 'data&data').as_str() == _url
