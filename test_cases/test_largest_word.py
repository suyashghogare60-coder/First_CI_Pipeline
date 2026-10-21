import sys
from pathlib import Path
import importlib
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"codes"))

module = importlib.import_module("largest_word")
largest_word = module.largest_word


def test_simple_sentence():
    assert largest_word("I love programming") == "programming"


def test_punctuation_is_ignored():
    assert largest_word("Hello, world!") == "Hello"


def test_tie_returns_first_word():
    assert largest_word("cat dog bat") == "cat"


def test_single_word():
    assert largest_word("Python") == "Python"


def test_empty_sentence():
    assert largest_word("") == ""