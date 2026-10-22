from importlib import import_module

module = import_module("29_armstrong_number")
is_armstrong = module.is_armstrong


def test_armstrong_number():
    assert is_armstrong(153) == True


def test_non_armstrong_number():
    assert is_armstrong(123) == False


def test_single_digit_number():
    assert is_armstrong(7) == True


def test_negative_number():
    assert is_armstrong(-153) == False


def test_zero():
    assert is_armstrong(0) == True