import pytest
from test1 import years_deposit

@pytest.fixture
def deposit_data():
    return [
        (1000, 10, 2593,74),
        (3000, 30, 52348,21),
        (1354, 5, 2180,63),
    ]


@pytest.mark.positive
def test_years_deposit(deposit_data):
    for amount, years, expected in deposit_data:
        assert years_deposit(amount,years) == expected


@pytest.mark.none("amount, years, expected",
[
    (0, 5, 0.00),
    (0, 1243, 0.00)
])
def deposit_none(amount, years, expected):
    assert years_deposit(amount,years) == expected


@pytest.mark.fail("amount, years",
[
    (1000, -2),
    (-2000, 10)
])
def deposit_fail(amount, years, expected):
    assert years_deposit(amount,years) == expected



