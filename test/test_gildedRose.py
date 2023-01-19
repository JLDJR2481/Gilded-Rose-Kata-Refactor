from src.gildedRose import *
from test.test_dias import *
import pytest


@pytest.fixture
def tienda():
    test_gildedRose = GildedRose(dayOne)
    return test_gildedRose


def test_updateInventory(tienda):
    for i in range(1, 30):
        tienda.updateInventory()

    for j in range(0, 9):
        assert tienda.items[j].name == dayThirty[j].name
