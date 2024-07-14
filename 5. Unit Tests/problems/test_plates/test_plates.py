from plates import is_valid


def test_valid():
    assert is_valid("CS50") == True


def test_zero_first():
    assert is_valid("CS05") == False


def test_number_in_the_middle():
    assert is_valid("CS50P") == False


def test_punctuation():
    assert is_valid("PI3.14") == False


def test_minimum_length():
    assert is_valid("H") == False


def test_maximum_length():
    assert is_valid("OUTATIME") == False


def test_starts_with_number():
    assert is_valid("2CS50") == False


def test_starts_with_letters():
    assert is_valid("A1") == False
