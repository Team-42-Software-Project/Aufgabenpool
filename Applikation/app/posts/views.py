import os
import secrets
import sys
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.posts.forms import PostForm
from app.users.forms import LoginForm, RegistrationForm
from app.users.models import User
from app.posts.models import Post
from app.topics.models import Topic
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
    topiclist = Topic.query.filter_by(user_id=current_user.id).all()
    return render_template('posts/new_post.html', title= 'Neue Aufgabe', form=form, topiclist=topiclist, legend='Neue Aufgabe')



@postmod.route('/entries/')
def entries():   
       #posts= Post.query.all()
       postlist = Post.query.filter_by(user_id=current_user.id).all()
       return render_template('posts/entries.html', posts=postlist)

@postmod.route('/entries/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit(id):
    post= Post.query.get_or_404(id)
    form =PostForm(subject=post.subject, topic=post.topic, level=post.level, text=post.text)
    if form.validate_on_submit():
        post.subject=form.subject.data
        post.topic= form.topic.data
        post.level=form.level.data
        post.text=form.text.data
        
        db.session.commit()
        flash('Aufgabe geändert', 'success')
        return redirect(url_for('posts.entries'))
    topiclist = Topic.query.filter_by(user_id=current_user.id).all()
    return render_template('posts/new_post.html', title= 'Aufgabe ändern', form=form, topiclist=topiclist, legend='Aufgabe ändern')


@postmod.route('/entries/delete/<int:id>')
@login_required
def delete (id):
    post= Post.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts/entries/')










