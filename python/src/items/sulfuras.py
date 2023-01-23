from src.items.normalItem import *


class Sulfuras(NormalItem):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def updateQuality(self):
        if self.quality == 80:
            pass
        else:
            print("Quality de {name} es distinta de 80".format(
                name=self.__class__.__name__))
