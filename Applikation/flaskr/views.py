import os
import secrets
from flask import render_template
from flaskr import app, db #bycrypt


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home2():
    return render_template('home2.html')


  