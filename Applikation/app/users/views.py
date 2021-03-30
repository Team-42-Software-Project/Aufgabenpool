import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.users.forms import RegistrationForm, LoginForm, TestForm
from app.users.models import User
from flask_login import login_user, current_user, logout_user, login_required


mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/register/', methods=['GET', 'POST'] )
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home2'))

    form=RegistrationForm()
    if form.validate_on_submit():
            hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user=User(username=form.username.data, email=form.email.data, password=hashed_password) 
            if form.image_file.data:
                img_file= save_profile_pic(form.image_file.data)
                user.image_file=img_file
            else:
                user.image_file="default.png"
            db.session.add(user)
            db.session.commit()
            flash(f'Account wurde erstellt, Sie können sich einloggen', 'success')
            return redirect(url_for('users.login')) 


    return render_template('users/register.html', form=form)


@mod.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home2'))

    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home2'))
        else:
            flash(f'Ckeck email and password!', 'danger') 

    return render_template('users/login.html', title='Login', form=form)

@mod.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

@mod.route('/view_users/')
def users():   
       users= User.query.all()
       return render_template('users/view_users.html', users=users)



def save_profile_pic(profile_pic):
    random_hex_code=secrets.token_hex(8)
    _, f_ext= os.path.splitext(profile_pic.filename)
    hex_picture_name= random_hex_code + f_ext
    picture_path=os.path.join(app.root_path, 'static/profile_pics', hex_picture_name)

    output_size=(60, 60)
    image= Image.open(profile_pic)
    image.thumbnail(output_size)
    image.save(picture_path)

    return hex_picture_name

