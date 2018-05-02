from rate.dates import CustomDate
from datetime import date

_date: str = '2018-04-14'


def test_today() -> None:
    assert CustomDate(str(date.today())).date() == str(date.today()).replace('-', '')


def test_date() -> None:
    assert CustomDate(_date).date() == '20180414'
