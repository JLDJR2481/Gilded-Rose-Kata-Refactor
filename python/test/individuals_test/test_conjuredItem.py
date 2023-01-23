from src.items.conjuredItems import *
import pytest


@pytest.fixture
def conjured_bow():

    test_conjured_bow = Conjured("Conjured bow", 20, 40)

    return test_conjured_bow


def test_updateQuality(conjured_bow):

    test_quality = 40
    test_sell_in = 20

    for i in range(0, 20):
        if test_sell_in < 0:
            test_quality -= 4

        if test_quality < 0:
            test_quality = 0

        elif test_sell_in >= 0:
            test_quality -= 2

        conjured_bow.updateQuality()
        test_sell_in -= 1

        assert conjured_bow.quality == test_quality
        assert conjured_bow.sell_in == test_sell_in
