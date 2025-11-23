from task5 import combine_dicts
def test_1():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 2, "c": 3, "d": 4}

def test_2():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 99, "c": 3}
    assert combine_dicts(d1, d2) == {"a": 1, "b": 99, "c": 3}

def test_3():
    d1 = {}
    d2 = {"x": 10}
    assert combine_dicts(d1, d2) == {"x": 10}

def test_4():
    d1 = {"x": 10}
    d2 = {}
    assert combine_dicts(d1, d2) == {"x": 10}

def test_5():
    assert combine_dicts({}, {}) == {}

def test_6():
    d1 = {"a": 1, "b": 2}
    d2 = {"c": 3, "d": 4}
    result = combine_dicts(d1, d2)
    assert list(result.keys()) == ["a", "b", "c", "d"]
# pytest -v