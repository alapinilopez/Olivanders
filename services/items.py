itemList = ["Aged Brie", "Sulfuras", "Conjured Mana Cake", "BacksStage Passes"]

def items():
    totalItems = ""
    for item in itemList:
        totalItems += item + ", "
    return totalItems

items()