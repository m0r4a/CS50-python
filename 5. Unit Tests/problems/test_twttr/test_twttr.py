from twttr import shorten
from pytest import raises


def test_regular():
    assert shorten("twitter") == "twttr"


def test_capitals():
    assert shorten("TWITTER") == "TWTTR"


def test_punctuation():
    assert shorten("twitt.er") == "twtt.r"


def test_int_string():
    assert shorten("twitter1") == "twttr1"


def test_only_int():
    with raises(TypeError):
        shorten(2)
