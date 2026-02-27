from task3 import is_palindrome
def test_1():
    assert is_palindrome("шалаш") is True

def test_2():
    assert is_palindrome("python") is False

def test_3():
    assert is_palindrome(12321) is True

def test_4():
    assert is_palindrome(12345) is False

def test_5():
    assert is_palindrome("БольшойСлон") is True

def test_6():
    assert is_palindrome("") is True

def test_7():
    assert is_palindrome("a") is True

def test_8():
    assert is_palindrome("черное небо") is False
# pytest -v