from rate.dates import CustomDate
from datetime import date

_date: str = '2018-04-14'


def test_today() -> None:
    assert CustomDate(str(date.today())).get() == str(date.today()).replace('-', '')


def test_date() -> None:
    assert CustomDate(_date).get() == '20180414'
