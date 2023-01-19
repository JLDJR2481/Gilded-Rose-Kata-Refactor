from src.items.normalItem import *
import pytest


@pytest.fixture
def vest():

    test_vest = NormalItem("+5 Dexterity Vest", 10, 20)

    return test_vest


def test_updateQuality(vest):

    test_quality = 20
    test_sell_in = 10

    for i in range(0, 20):
        if test_sell_in < 0:
            test_quality -= 2

        if test_quality < 0:
            test_quality = 0

        elif test_sell_in >= 0:
            test_quality -= 1

        vest.updateQuality()
        test_sell_in -= 1

        assert vest.quality == test_quality
        assert vest.sell_in == test_sell_in
