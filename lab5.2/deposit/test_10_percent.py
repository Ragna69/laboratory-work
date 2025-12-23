import pytest
from test1 import years_deposit

def test_basic_deposit():
    try:
        assert years_deposit(3, 1000) == 1331.00
        assert years_deposit(5, 1354) == 2180.63
    except Exception as e:
        pytest.fail(f"Ошибка {e}")

def test_zero_deposit():
    try:
        assert years_deposit(0, 1000) == 1000.00   # исправлено
        assert years_deposit(1234, 0) == 0.00
    except Exception as e:
        pytest.fail(f"Ошибка {e}")

def test_negative_value():
    try:
        years_deposit(-2, 1345)
        years_deposit(2, -1345)
    except ValueError as e:
        assert "не могут быть отрицательными" in str(e)
    else:
        pytest.fail("Ожидалось исключение")

@pytest.fixture
def deposit_data():
    return [(1000, 10, 2593.74),(3000, 30, 52348.21), (1354, 5, 2180.63)]

def test_fixture(deposit_data):
    for amount, years, expected in deposit_data:
        result = years_deposit(years, amount)
        assert result == expected

@pytest.mark.parametrize("years, amount, expected",[(1,1000, 1100.00),(2, 1000, 1210.00)])
def test_parametrize(years, amount, expected):
    try:
        result = years_deposit(years, amount)
    except Exception as e:
        pytest.fail(f"Ошибка {e}")
    else:
        assert result == expected

@pytest.mark.skip(reason="Пропуск")
def test_skip_deposit():
    try:
        assert years_deposit(7, 500) == 973.50
    finally:
        pass

@pytest.mark.xfail(reason="Пропуск")
def test_deposit_fail():
    try:
        assert years_deposit(1, 1000) == 4000
    except ValueError as e:
        raise
    else:
        pytest.fail("Ожидалась ошибка")

@pytest.mark.new(reason="Пропуск")
def test_basic_deposit():
    try:
        assert years_deposit(3, 1000) == 1331.00
    except Exception as e:
        pytest.fail(f"Ошибка {e}")



