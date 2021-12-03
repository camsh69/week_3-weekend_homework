from app import app
from flask import render_template
from models.items import Items
from models.items_list import items

@app.route("/")
def index():
    return render_template('index.html', items=items)
