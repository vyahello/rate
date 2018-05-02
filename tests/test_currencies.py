from rate.currencies import BRL, TJS, RUB, RSD, BYN, AUD, EUR, PLN


def test_brl() -> None:
    assert BRL().__str__() == 'brl'


def test_tjs() -> None:
    assert TJS().__str__() == 'tjs'


def test_rub() -> None:
    assert RUB().__str__() == 'rub'


def test_rsd() -> None:
    assert RSD().__str__() == 'rsd'


def test_byn() -> None:
    assert BYN().__str__() == 'byn'


def test_aud() -> None:
    assert AUD().__str__() == 'aud'


def test_eur() -> None:
    assert EUR().__str__() == 'eur'


def test_pln() -> None:
    assert PLN().__str__() == 'pln'
