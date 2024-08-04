from seasons import date_parser
from datetime import date
from pytest import raises


def test_valid():
    assert date_parser("2004-08-10") == date(2004, 8, 10)


def test_invalid_date():
    with raises(SystemExit):
        date_parser("invalid-date")


def test_invalid_month():
    with raises(SystemExit):
        date_parser("2004-13-10")


def test_invalid_day():
    with raises(SystemExit):
        date_parser("2004-08-33")
