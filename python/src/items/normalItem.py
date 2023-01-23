from src.items.item import *
from src.items.interfaz import *


class NormalItem(Item, Interfaz):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def getName(self):
        return self.name

    def getSellIn(self):
        return self.sell_in

    def getQuality(self):
        return self.quality

    def setName(self, second_name):
        self.name = second_name

    def setSellIn(self):
        self.sell_in = self.sell_in - 1

    def setQuality(self, value):

        self.quality += value

        if self.quality > 50:
            self.quality = 50

        elif self.quality < 0:
            self.quality = 0

        assert 50 >= self.quality >= 0

    def updateQuality(self):

        if self.sell_in >= 0:
            self.setQuality(-1)

        else:
            self.setQuality(-2)

        self.setSellIn()
