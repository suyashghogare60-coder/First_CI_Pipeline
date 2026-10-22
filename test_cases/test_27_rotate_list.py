from importlib import import_module

module = import_module("27_rotate_list")
rotate_list = module.rotate_list


def test_rotate_right():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]


def test_k_larger_than_length():
    assert rotate_list([1, 2, 3], 5) == [2, 3, 1]


def test_negative_k_rotates_left():
    assert rotate_list([1, 2, 3, 4, 5], -2) == [3, 4, 5, 1, 2]


def test_empty_list():
    assert rotate_list([], 3) == []


def test_original_list_unchanged():
    items = [1, 2, 3, 4, 5]
    rotate_list(items, 2)
    assert items == [1, 2, 3, 4, 5]

# python -m pytest .\test_cases\test_27_rotate_list.py