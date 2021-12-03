from models.items import *

item1 = Items("Milk", 1.00, 1, True)
item2 = Items("Cheese", 2.25, 1, False)

items = [item1, item2]

def add_new_item(item):
    items.append(item)


