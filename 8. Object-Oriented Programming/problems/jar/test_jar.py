import pytest
from jar import Jar


def test_initial_capacity():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_deposit_valid():
    jar = Jar(10)
    jar.deposit(5)
    assert jar.size == 5


def test_deposit_exceed_capacity():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError, match="You can't deposit more cookies than the maximum capacity"):
        jar.deposit(6)


def test_withdraw_valid():
    jar = Jar(10)
    jar.deposit(5)
    jar.withdraw(2)
    assert jar.size == 3


def test_withdraw_not_enough_cookies():
    jar = Jar(10)
    jar.deposit(5)
    with pytest.raises(ValueError, match="Not enough cookies in the jar"):
        jar.withdraw(6)


def test_invalid_deposit_type():
    jar = Jar(10)
    with pytest.raises(ValueError, match="Invalid number of cookies"):
        jar.deposit("five")


def test_invalid_withdraw_type():
    jar = Jar(10)
    with pytest.raises(ValueError, match="Invalid number of cookies"):
        jar.withdraw("three")


def test_invalid_capacity_type():
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        Jar("ten")


def test_negative_capacity():
    with pytest.raises(ValueError, match="Capacity must be a non-negative integer"):
        Jar(-10)


def test_negative_deposit():
    jar = Jar(10)
    with pytest.raises(ValueError, match="Invalid number of cookies"):
        jar.deposit(-5)


def test_negative_withdraw():
    jar = Jar(10)
    with pytest.raises(ValueError, match="Invalid number of cookies"):
        jar.withdraw(-3)
