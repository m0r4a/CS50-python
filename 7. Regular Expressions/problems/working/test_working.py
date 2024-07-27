from working import convert
from pytest import raises


def test_none_zeros():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_full_zeros():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_minutes_right():
    assert convert("10 AM to 8:50 PM") == "10:00 to 20:50"


def test_minutes_left():
    assert convert("10:30 PM to 8 AM") == "22:30 to 08:00"


def test_12_AM():
    assert convert("12 AM to 8 PM") == "00:00 to 20:00"


def test_12_PM():
    assert convert("12 PM to 8 AM") == "12:00 to 08:00"


def test_more_than_59_minutes():
    with raises(ValueError):
        convert("9:60 AM to 5:60 PM")


def test_not_colon_without_minutes():
    with raises(ValueError):
        convert("9 AM - 5 PM")


def test_not_colon_with_minutes():
    with raises(ValueError):
        convert("09:00 AM - 17:00 PM")
