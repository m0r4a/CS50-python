from bank import value


def test_hello_lower():
    assert value("hello") == 0


def test_hello():
    assert value("Hello") == 0


def test_starts_with_h():
    assert value("Hey!") == 20


def test_doesnt_have_h():
    assert value("What's up?") == 100
