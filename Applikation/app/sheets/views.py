import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.posts.forms import PostForm
from app.users.forms import LoginForm, RegistrationForm
from app.sheets.forms import SheetForm, SelectTopicForm
from app.users.models import User
from app.posts.models import Post
from app.topics.models import Topic
#from app.sheets.models import Sheet
from flask_login import login_user, current_user, login_required

sheetmod = Blueprint('sheets', __name__, url_prefix='/sheets')

@sheetmod.route('/new_sheet/', methods=['GET', 'POST'])
@login_required
def new_sheet():
    form =SelectTopicForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.validate_on_submit())
        selected_topic = form.topic.data
        flash('Thema wurde gewählt', 'success')
        #return "Something happend"
        posts= Post.query.all()
        postlist = Post.query.filter_by(user_id=current_user.id)
        print(form.topic.data)
        postlist = Post.query.filter_by(user_id=current_user.id,topic = selected_topic).order_by(Post.level).all()
        
        return render_template('sheets/new_sheet2.html', posts=postlist,selected_topic=selected_topic)
    if request.method =='POST':
        
        selected_post_id = request.form.getlist('question')
        my_selected_postlist = Post.query.filter(Post.id.in_(selected_post_id)).order_by(Post.level).all()
        return render_template('sheets/new_sheet3.html', posts=my_selected_postlist,selected_topic=form.topic.data)
   
    topiclist = Topic.query.filter_by(user_id=current_user.id).all()
    return render_template('sheets/new_sheet.html', title= 'Neues Aufgabenblatt zusammenstellen', form=form, topiclist=topiclist, legend='Neues Aufgabenblatt')





