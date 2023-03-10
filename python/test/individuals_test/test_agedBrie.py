from src.items.agedBrie import *
import pytest


@pytest.fixture
def brie():

    test_brie = AgedBrie("Aged Brie", 2, 0)

    return test_brie


def test_updateQuality(brie):

    test_quality = 0
    test_sell_in = 2

    for i in range(0, 12):
        if test_sell_in > 0:
            test_quality += 1

        elif test_quality < 0:
            test_quality = 0

        elif test_sell_in <= 0:
            test_quality += 2

        brie.updateQuality()
        test_sell_in -= 1

        assert brie.sell_in == test_sell_in

        assert brie.quality == test_quality
