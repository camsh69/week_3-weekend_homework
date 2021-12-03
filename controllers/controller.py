from app import app
from flask import render_template, request
from models.items_list import items
from models.items import Items

@app.route('/shoppinglist')
def index():
    return render_template('index.html', title="Shopping List", items=items)

@app.route('/shoppinglist', methods=['POST'])
def add_item():
    pass
