from trippingarcher import app
from flask import render_template
from trippingarcher import Item

@app.route("/")
def index():
    return render_template('index.html')
@app.route("/fridge")
def fridge():
    return render_template('fridge.html', items=Item.query.all())