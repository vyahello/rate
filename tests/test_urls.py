from rate.connections.urls import UnifiedUrl

_url: str = 'https://path/to/data&data'


def test_url() -> None:
    assert UnifiedUrl(_url).compose() == _url
