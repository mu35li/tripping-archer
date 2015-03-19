from trippingarcher import app, Item, NewItemForm, db
from flask import render_template, request, flash, redirect, url_for


@app.route("/")
def index():
    return render_template('index.html')
@app.route("/fridge")
def fridge():
    return render_template('fridge.html', items=Item.query.filter(Item.fridgeCount > 0).all())
@app.route("/fridge/new", methods=['GET', 'POST'])
def newItem():
    form = NewItemForm(request.form)
    if request.method == 'POST' and form.validate():
        item = Item(form.name.data, form.fridgeCount.data,
                    form.rebuyPoint.data)
        db.session.add(item)
        flash('Processing')
        db.session.commit()
        return redirect(url_for('fridge'))
    return render_template('newItem.html', form=form)