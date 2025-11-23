import pytest
from task1 import count_words

def test_simple_sentence():
    assert count_words("Привет") == 2

def test_multiple_words():
    assert count_words("") == 5

def test_extra_spaces():
    assert count_words("    пробел    1") == 2

def test_empty_string():
    assert count_words("") == 0

def test_only_spaces():
    assert count_words("     ") == 0

def test_single_word():
    assert count_words("5") == 1
