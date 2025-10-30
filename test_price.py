import pytest

prices = [("basic", 10), ("pro", 20), ("enterprise", 30)]

@pytest.mark.parametrize("name,price", prices, ids=[p[0] for p in prices])
def test_price_tiers(name, price):
    assert price > 0