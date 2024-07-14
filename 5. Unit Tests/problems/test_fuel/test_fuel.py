
from fuel import convert, gauge
from pytest import raises

### Convert ###


def test_success():
    assert convert("1/2") == 50


def test_valueError():
    with raises(ValueError):
        convert("2/1")


def test_zeroDivisionError():
    with raises(ZeroDivisionError):
        convert("1/0")


def test_string():
    with raises(ValueError):
        convert("cat")


### gauge ###

def test_empty_fuel():
    assert gauge(1) == "E"


def test_full_fuel():
    assert gauge(99) == "F"


def test_regular_fuel():
    assert gauge(50) == "50%"


def test_string_gauge():
    with raises(TypeError):
        gauge("cat")
