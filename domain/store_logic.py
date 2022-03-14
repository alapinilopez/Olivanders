class GildedRose(object):
    def __init__(self, stock):
        self.stock = stock

    def updateQuality(self):
        for item in self.stock:
                item.updateQuality()


class Item:
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality

    def setSellIn(self):
        self.sellIn = self.sellIn - 1

    def setQuality(self, value):
        if self.quality + value > 50:
            self.quality = 50
        elif self.quality + value >= 0:
            self.quality = self.quality + value
        else:
            self.quality = 0

    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(-1)
        else:
            self.setQuality(-2)
        self.setSellIn()


class Updatable():
    def updateQuality(self):
        pass


class NormalItem(Item, Updatable):
    def __init__(self, name, sellIn, quality):
        super().__init__(self, name, sellIn, quality)


class Sulfuras(Item):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, value):
        return super().setQuality(value)
    
    def setSellIn(self):
        return super().setSellIn()
    
    def updateQuality(self):
        self.quality == 80


class Concert(Item):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, value):
        return super().setQuality(value)
    
    def setSellIn(self):
        return super().setSellIn()


class AgedBrie(Item):
    def __init__(self, name, sellIn, quality):
        super().__init__(name, sellIn, quality)
    
    def setQuality(self, value):
        return super().setQuality(value)
    
    def setSellIn(self):
        return super().setSellIn()
    
    def updateQuality(self):
        if self.sellIn > 0:
            self.setQuality(1)
        else:
            self.setQuality(2)
    
    def updateQuality(self):
        if self.sellIn > 10:
            self.setQuality(1)
        elif self.sellIn <= 10:
            self.setQuality(2)
        elif self.sellIn <= 5:
            self.setQuality(3)
        else: 0
        self.setSellIn()
