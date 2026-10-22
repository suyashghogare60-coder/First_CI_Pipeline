from importlib import import_module

module = import_module("28_set_intersection")
set_intersection = module.set_intersection


def test_common_elements():
    assert set_intersection({1, 2, 3}, {2, 3, 4}) == {2, 3}


def test_no_common_elements():
    assert set_intersection({1, 2}, {3, 4}) == set()


def test_identical_sets():
    assert set_intersection({1, 2, 3}, {1, 2, 3}) == {1, 2, 3}


def test_empty_set():
    assert set_intersection(set(), {1, 2, 3}) == set()


def test_single_common_element():
    assert set_intersection({1, 2, 3}, {3, 4, 5}) == {3}


# python -m pytest .\test_cases\test_28_set_intersection.py