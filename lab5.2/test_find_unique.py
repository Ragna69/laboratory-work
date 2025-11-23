import pytest
from task2 import find_unique

def test_simple_list():
    assert find_unique([1, 2, 2, 3, 4, 4]) == [1, 3]

def test_all_unique():
    assert find_unique([10, 20, 30]) == [10, 20, 30]

def test_no_unique():
    assert find_unique([5, 5, 6, 6, 7, 7]) == []

def test_strings():
    assert find_unique(["яблоко", "привет", "стол", "компьютер"]) == ["яблоко", "привет", "стол", "компьютер"]

def test_mixed_types():
    assert find_unique([1, "а", 2, "а", 3]) == [1, 2, 3]

def test_empty_list():
    assert find_unique([]) == []

def test_single_element():
    assert find_unique([52]) == [52]
