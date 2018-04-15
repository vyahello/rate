from rate.dates import CustomDate
from datetime import date

_date = '2018-04-14'


def test_today():
    assert CustomDate(str(date.today())).date() == str(date.today()).replace('-', '')


def test_date():
    assert CustomDate(_date).date() == '20180414'
