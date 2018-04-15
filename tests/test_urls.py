from rate.connections.urls import HttpsUrl

_url = 'https://path/to/data&data'


def test_url():
    assert HttpsUrl('path/to/', 'data&data').as_str() == _url
