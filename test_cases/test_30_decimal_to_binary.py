from importlib import import_module
import pytest

module = import_module("30_decimal_to_binary")
decimal_to_binary = module.decimal_to_binary


def test_convert_ten():
    assert decimal_to_binary(10) == "1010"


def test_convert_zero():
    assert decimal_to_binary(0) == "0"


def test_convert_one():
    assert decimal_to_binary(1) == "1"


def test_convert_eight():
    assert decimal_to_binary(8) == "1000"


def test_negative_number():
    with pytest.raises(ValueError):
        decimal_to_binary(-5)