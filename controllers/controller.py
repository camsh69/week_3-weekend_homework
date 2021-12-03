from app import app
from flask import render_template, request, redirect
from models.items_list import items, add_new_item, total_price, total_items
from models.items import Items

@app.route('/shoppinglist')
def index():
    return render_template('index.html', title="Shopping List", items=items, 
    total_price=total_price(items), total_items=(total_items(items)))

@app.route('/shoppinglist', methods=['POST'])
def add_item():
    name_of_item = request.form['name_of_item']
    input_price = float(request.form['price'])
    price = "{:.2f}".format(input_price)
    quantity = int(request.form['quantity'])
    bought = True if 'bought' in request.form else False
    new_item = Items(name_of_item, price, quantity, bought)
    add_new_item(new_item)
    return redirect ('/shoppinglist')