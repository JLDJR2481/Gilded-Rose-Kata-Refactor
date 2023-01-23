from src.items.sulfuras import *
import pytest


@pytest.fixture
def sulfur():

    test_sulfuras = Sulfuras("Sulfuras, Hand of Ragnaros", -1, 80)

    return test_sulfuras


def test_updateQuality(sulfur):

    for i in range(0, 15):
        sulfur.updateQuality()

        assert sulfur.sell_in == -1
        assert sulfur.quality == 80
