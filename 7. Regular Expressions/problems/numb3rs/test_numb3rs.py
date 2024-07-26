from numb3rs import validate


def test_valid_ipv4():
    assert validate("192.168.0.1") is True
    assert validate("0.0.0.0") is True
    assert validate("255.255.255.255") is True
    assert validate("127.0.0.1") is True


def test_string():
    assert validate("cat") is False


def test_invalid_ipv4():
    assert validate("999.999.999.999") is False
    assert validate("256.256.256.256") is False
    assert validate("192.168.0.256") is False
    assert validate("192.168.0.-1") is False


def test_empty_string():
    assert validate("") is False


def test_invalid_characters():
    assert validate("192.168.0.1a") is False
    assert validate("abc.def.ghi.jkl") is False


def test_incomplete_ipv4():
    assert validate("192.168.1") is False
    assert validate("192.168") is False
    assert validate("192") is False


def test_extra_characters():
    assert validate("192.168.0.1 extra") is False
    assert validate("192.168.0.1 ") is False


def test_non_ip_string():
    assert validate("not.an.ip") is False
    assert validate("hello.world") is False
