from models.items import *

item1 = Items("Milk", 1.25, 1, True)
item2 = Items("Cheese", 2.25, 1, False)

items = [item1, item2]

def add_new_item(item):
    items.append(item)

def total_price(items):
    total = 0
    for item in items:
        total += item.price
    return "{:.2f}".format(total)

def total_items(items):
    return len(items)