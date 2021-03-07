import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.posts.forms import PostForm
from app.users.forms import LoginForm, RegistrationForm
from app.users.models import User
from app.posts.models import Post
from flask_login import login_user, current_user, login_required

postmod = Blueprint('posts', __name__, url_prefix='/posts')

@postmod.route('/new_post/', methods=['GET', 'POST'])
@login_required
def new_post():
    form =PostForm()
    if form.validate_on_submit():
        post= Post(subject=form.subject.data, topic= form.topic.data, level=form.level.data, 
        text=form.text.data, autor=current_user)
        
        db.session.add(post)
        db.session.commit()
        flash('Aufgabe wurde erstellt', 'success')
        return redirect(url_for('posts.entries'))
    
    return render_template('posts/new_post.html', title= 'Neue Aufgabe', form=form, legend='Neue Aufgabe')



@postmod.route('/entries/')
def entries():   
       posts= Post.query.all()
       return render_template('posts/entries.html', posts=posts)












