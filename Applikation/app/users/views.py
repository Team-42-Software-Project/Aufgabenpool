import os
import secrets
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.users.forms import RegistrationForm

from app.users.models import User


mod = Blueprint('users', __name__, url_prefix='/users')

@mod.route('/register/', methods=['GET', 'POST'] )
def register():
    #if current_user.is_authenticated:
        #return redirect(url_for('home2'))

    form=RegistrationForm()
    if form.validate_on_submit():
            hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user=User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account wurde gemacht, Sie können sich einloggen', 'success')
            #return redirect(url_for('users.login')) 
            return "hier muss man zum Login kommen TODO."

    return render_template('users/register.html', form=form)