from src.items.normalItem import *


class Conjured(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def updateQuality(self):

        if self.sell_in >= 0:
            self.setQuality(-2)

        else:
            self.setQuality(-4)

        self.setSellIn()
