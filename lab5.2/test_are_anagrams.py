from task4 import are_anagrams
def test_1():
    assert are_anagrams("listen", "silent") is True

def test_2():
    assert are_anagrams("привет", "ветрип") is False

def test_3():
    assert are_anagrams("Race", "Care") is True

def test_4():
    assert are_anagrams("еду домой", "доеудойм") is True

def test_5():
    assert are_anagrams("", "") is True

def test_6():
    assert are_anagrams("", "abc") is False

def test_7():
    assert are_anagrams("аабб", "аб") is False

def test_8():
    assert are_anagrams("кот", "ток") is True
# pytest -v