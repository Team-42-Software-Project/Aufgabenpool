
import os
import secrets
from PIL import Image
from flask import render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from flask_login import login_user, current_user, logout_user, login_required



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home2():
   
    return render_template('home2.html')





def save_picture(form_picture):
    random_hex=secrets.token_hex(8)
    _, f_ext= os.path.splitext(form_picture.filename)
    picture_fn= random_hex + f_ext
    picture_path=os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size=(50, 50)
    i= Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


