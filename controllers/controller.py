from app import app
from flask import render_template, request, redirect
from models.items_list import *
from models.items import Items


@app.route('/shoppinglist')
def index():
    return render_template('index.html', title="My Shopping List", items=items,
                           total_price=total_price(items), total_items=total_items(items))


@app.route('/shoppinglist', methods=['POST'])
def add_item():
    name_of_item = request.form['name_of_item']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    bought = True if 'bought' in request.form else False
    new_item = Items(name_of_item, price, quantity, bought)
    add_new_item(new_item)
    return redirect('/shoppinglist')


@app.route('/shoppinglist/delete/', methods=['POST'])
def remove_item_from_list():
    name_of_item = request.form['name_of_item']
    remove_item(name_of_item)
    return redirect('/shoppinglist')


@app.route('/shoppinglist/buy/', methods=['POST'])
def buy():
    name_of_item = request.form['name_of_item']
    buy_item(name_of_item)
    return redirect('/shoppinglist')
