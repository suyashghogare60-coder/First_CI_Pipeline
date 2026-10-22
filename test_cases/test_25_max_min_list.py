from importlib import import_module
import pytest

module = import_module("25_max_min_list")
find_max_min = module.find_max_min


def test_normal_list():
    assert find_max_min([4, 9, 1, 7]) == (9, 1)


def test_negative_numbers():
    assert find_max_min([-5, -2, -9, -1]) == (-1, -9)


def test_duplicate_numbers():
    assert find_max_min([4, 4, 4]) == (4, 4)


def test_single_element():
    assert find_max_min([7]) == (7, 7)


def test_empty_list():
    with pytest.raises(ValueError):
        find_max_min([])

# python -m pytest .\test_cases\test_25_max_min_list.py