class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                continue

            degrade = 1
            if "Conjurado" in item.name:
                degrade = 2 #degrade duas vezes mais rapido do que um item normal

            #agedbrie melhora
            if item.name == "Aged Brie":
                if item.quality < 50:
                    item.quality += 1

            #backstage melhora
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if item.quality < 50:
                    item.quality += 1
                    if item.sell_in <= 10 and item.quality < 50:
                        item.quality += 1
                    if item.sell_in <= 5 and item.quality < 50:
                        item.quality += 1

            #os dois tipos de itens perdem qualidade
            else:
                item.quality -= degrade
                if item.quality < 0:
                    item.quality = 0

            item.sell_in -= 1  # prazo menor!

            #regras depois de expira
            if item.sell_in < 0:
                if item.name == "Aged Brie":
                    if item.quality < 50:
                        item.quality += 1
                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    item.quality = 0
                else:
                    item.quality -= degrade
                    if item.quality < 0:
                        item.quality = 0
