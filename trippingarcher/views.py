from trippingarcher import app, Item, NewItemForm, db, EditItemForm
from flask import render_template, request, flash, redirect, url_for
from sqlalchemy import update


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/fridge")
def fridge():
    return render_template('fridge.html', items=Item.query.filter(Item.deleted == 0).all())

@app.route("/fridge/new", methods=['GET', 'POST'])
def newItem():
    form = NewItemForm(request.form)
    if request.method == 'POST' and form.validate():
        existingItem = Item.query.filter(Item.name == form.name.data).first()
        if existingItem is None:
            item = Item(form.name.data, form.fridgeCount.data, form.rebuyPoint.data, 0)
            db.session.add(item)
        else:
            existingItem.fridgeCount = form.fridgeCount.data
        flash('Processing')
        db.session.commit()
        return redirect(url_for('fridge'))
    return render_template('newItem.html', form=form, items=Item.query.filter(Item.deleted == 1).all())

@app.route("/fridge/delete", methods=['GET'])
def deleteItem():
    itemId = request.args.get('itemId', '')
    item = Item.query.get(itemId)
    item.deleted = 1
    db.session.commit()
    return redirect(url_for('fridge'))

@app.route("/fridge/updateItem", methods=['GET'])
def updateItem():
    if request.args.get('count', '') == '':
        return redirect(url_for('fridge'))
    else:
        itemId = request.args.get('itemId', '')
        item = Item.query.get(itemId)
        item.fridgeCount = request.args.get('count', '')
        item.deleted = 0
        db.session.commit()
        return redirect(url_for('fridge'))

@app.route("/fridge/editItem", methods=['GET', 'POST'])
def editItem():
    itemId = request.args.get('itemId', '')
    # if itemId == '':
    #     return redirect(url_for('fridge'))
    form = EditItemForm(request.form)
    if request.method == 'POST' and form.validate(): 
        name = form.name.data
        count = form.fridgeCount.data
        rebuy = form.rebuyPoint.data 
        if name != '' and count  != '' and rebuy != '':
            item = Item.query.get(itemId)
            item.name = name
            item.fridgeCount = count
            item.rebuyPoint = rebuy
            db.session.commit()
            return redirect(url_for('fridge'))
    return render_template('editItem.html', form=form, item= Item.query.get(itemId))

