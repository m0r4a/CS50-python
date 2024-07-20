from plates import is_valid


def test_valid():
    assert is_valid("CS50") is True


def test_zero_first():
    assert is_valid("CS05") is False


def test_number_in_the_middle():
    assert is_valid("CS50P") is False


def test_punctuation():
    assert is_valid("PI3.14") is False


def test_minimum_length():
    assert is_valid("H") is False


def test_maximum_length():
    assert is_valid("OUTATIME") is False


def test_starts_with_number():
    assert is_valid("2CS50") is False


def test_starts_with_letters():
    assert is_valid("A1") is False
