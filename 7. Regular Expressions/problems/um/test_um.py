from um import count


def test_zero():
    assert count("yummy") == 0


def test_one():
    assert count("um") == 1
    assert count("hello, um, world") == 1
    assert count("Um, thanks for the album") == 1


def test_two():
    assert count("Um, thanks, um...") == 2
