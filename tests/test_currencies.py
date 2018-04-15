from rate.currencies import BRL, TJS, RUB, RSD, BYN, AUD, EUR, PLN


def test_brl():
    assert BRL().__str__() == 'brl'


def test_tjs():
    assert TJS().__str__() == 'tjs'


def test_rub():
    assert RUB().__str__() == 'rub'


def test_rsd():
    assert RSD().__str__() == 'rsd'


def test_byn():
    assert BYN().__str__() == 'byn'


def test_aud():
    assert AUD().__str__() == 'aud'


def test_eur():
    assert EUR().__str__() == 'eur'


def test_pln():
    assert PLN().__str__() == 'pln'
