from task1 import count_words

def test_1():
    assert count_words("Привет") == 2

def test_2():
    assert count_words("") == 5

def test_3():
    assert count_words("    пробел    1") == 2

def test_4():
    assert count_words("") == 0

def test_5():
    assert count_words("     ") == 0

def test_6():
    assert count_words("5") == 1
# pytest -v