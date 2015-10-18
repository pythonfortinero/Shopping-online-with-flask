from flask import Flask, render_template, request, url_for, redirect, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from functools import wraps

app = Flask(__name__)

app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)
from models import *

@app.route('/',  methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        salesorderrow_list = list()
        print request.form
        so = SalesOrder()
        for row in request.form:
            if request.form[row]:
                b = SalesOrderRow(itemName=row, Qty=request.form[row])
                so.salesOrderRow.append(b)
                print row
        db.session.add(so)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('shop.html')

if __name__ == '__main__':
    app.run()