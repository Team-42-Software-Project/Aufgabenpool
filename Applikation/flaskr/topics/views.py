
import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flaskr import app, db, bcrypt 
from flaskr.topics.forms import TopicForm
from flaskr.users.models import User
from flaskr.posts.models import Post 
from flaskr.topics.models import Topic
from flask_login import login_user, current_user, logout_user, login_required

topicmod = Blueprint('topics', __name__, url_prefix='/topics')

@topicmod.route('/new_topic/', methods=[ 'GET','POST'])
@login_required
def new_topic():
    form =TopicForm()
    if form.validate_on_submit():
        add_topic_to_db(form)
        return redirect(url_for('topics.new_topic'))
    else:
        topics = Topic.query.filter_by(user_id=current_user.id).all()
        return render_template("topics/new_topic.html", topics=topics,form=form)
   
def add_topic_to_db(form):
    my_new_topic= Topic(content=form.topic.data, autor=current_user)       
    db.session.add(my_new_topic)
    db.session.commit()

def mytest(number):
    return number
    


