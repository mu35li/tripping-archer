
from flask import Flask, request, session, redirect, url_for, \
     abort, render_template, flash

from wtforms import Form, BooleanField, TextField, PasswordField, DecimalField, validators

from flask.ext.sqlalchemy import SQLAlchemy
# configuration
DATABASE = '/tmp/trippingarcher.db'
SECRET_KEY = 'hahaha'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/trippingarcher.db'
db = SQLAlchemy(app)

# from main.database import db_session

# @app.teardown_appcontext
# def shutdown_session(exception=None):
#     db_session.remove()
from trippingarcher.database import db_session

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



class Item(db.Model):
    __tablename__ = 'items'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    fridgeCount = db.Column(db.Float)
    rebuyPoint = db.Column(db.Float)

    def __init__(self, name, fridgeCount, rebuyPoint):
        self.name = name
        self.fridgeCount = fridgeCount
        self.rebuyPoint = rebuyPoint

    def __repr__(self):
        return '<Item %r>' % self.name

class ShoppingList(db.Model):
    __tablename__ = 'shoppingLists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), unique=True)
    createdAt = db.Column(db.Date)
    finishedAt = db.Column(db.Date)

    def __init__(self, name, createdAt, finishedAt):
        self.name = name
        self.createdAt = createdAt
        self.finishedAt = finishedAt

    def __repr__(self):
        return '<ShoppingList %r>' % self.name

class NewItemForm(Form):
    name = TextField('Name')
    fridgeCount = DecimalField('In fridge')
    rebuyPoint = DecimalField('When to rebuy')

import trippingarcher.views
