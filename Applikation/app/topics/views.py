
import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.topics.forms import TopicForm
from app.users.models import User
from app.posts.models import Post 
from app.topics.models import Topic
from flask_login import login_user, current_user, logout_user, login_required

topicmod = Blueprint('topics', __name__, url_prefix='/topics')

@topicmod.route('/new_topic/', methods=[ 'GET','POST'])
@login_required
def new_topic():
    form =TopicForm()
    if form.validate_on_submit():
        my_new_topic= Topic(content=form.topic.data)
        
        db.session.add(my_new_topic)
        db.session.commit()
        flash('Thema wurde hinzugefügt', 'success')
        return redirect(url_for('topics.new_topic'))
    else:
        topics = Topic.query.order_by(Topic.date_created).all()
        return render_template("topics/new_topic.html", topics=topics,form=form)
   
    