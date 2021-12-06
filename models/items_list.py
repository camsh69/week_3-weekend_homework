from models.items import *

item1 = Items("Milk", 1.25, 1, True)
item2 = Items("Cheese", 2.25, 1, False)

items = [item1, item2]


def add_new_item(item):
    items.append(item)


def total_price(items):
    total = 0.0
    for item in items:
        total += (item.price * item.quantity)
        if item.quantity >= 5:
            total -= (item.price/10) * item.quantity
    return "{:.2f}".format(total)


def total_items(items):
    total = 0
    for item in items:
        total += item.quantity
    return total


def remove_item(name_of_item):
    for item in items:
        if item.name_of_item == name_of_item:
            items.remove(item)


def buy_item(name_of_item):
    for item in items:
        if item.name_of_item == name_of_item:
            item.bought = True
