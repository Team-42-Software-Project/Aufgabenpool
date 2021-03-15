import os
import secrets
from PIL import Image
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.posts.forms import PostForm
from app.users.forms import LoginForm, RegistrationForm
from app.sheets.forms import SheetForm, SelectTopicForm, SelectSheetForm
from app.users.models import User
from app.posts.models import Post
from app.topics.models import Topic
from app.sheets.models import Sheet, SheetPost
from flask_login import login_user, current_user, login_required

sheetmod = Blueprint('sheets', __name__, url_prefix='/sheets')

@sheetmod.route('/new_sheet/', methods=['GET', 'POST'])
@login_required
def new_sheet():
    form =SelectTopicForm()
    if form.validate_on_submit():
        print(form.validate_on_submit())
        selected_topic = form.topic.data
        flash('Thema wurde gewählt', 'success')
        return redirect(url_for('sheets.new_sheet2',selected_topic=selected_topic))
    topiclist = Topic.query.filter_by(user_id=current_user.id).all()
    return render_template('sheets/new_sheet.html', title= 'Neues Aufgabenblatt zusammenstellen', form=form, topiclist=topiclist, legend='Neues Aufgabenblatt')


@sheetmod.route('/new_sheet2/', methods=['GET', 'POST'])
@login_required
def new_sheet2():
    selected_topic = request.args['selected_topic']
    postlist = Post.query.filter_by(user_id=current_user.id,topic = selected_topic).order_by(Post.level).all()   
    form =SheetForm()
    if form.validate_on_submit():
        selected_post_id = request.form.getlist('question')
        title = form.title.data
        my_selected_postlist = Post.query.filter(Post.id.in_(selected_post_id)).order_by(Post.level).all()
        newsheet= Sheet(title=form.title.data, topic= selected_topic, autor=current_user)
        db.session.add(newsheet)
        db.session.commit()
        for id in selected_post_id:
            new_sheet_post=SheetPost(post_id=id, sheet_id=newsheet.id)
            db.session.add(new_sheet_post)
            db.session.commit()
        return redirect(url_for('sheets.new_sheet3',selected_topic=selected_topic))
    return render_template('sheets/new_sheet2.html', posts=postlist,selected_topic=selected_topic, form=form)
    

@sheetmod.route('/new_sheet3/', methods=['GET', 'POST'])
@login_required
def new_sheet3():
    return render_template('sheets/new_sheet3.html')


@sheetmod.route('/view_sheet/', methods=['GET', 'POST'])
@login_required
def view_sheet():
    sheetlist = Sheet.query.filter_by(user_id=current_user.id).all()
    form = SelectSheetForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        print(form.id.data)
        return redirect(url_for('sheets.view_sheet2',selected_sheet = form.id.data))
    return render_template('sheets/view_sheet.html',sheetlist=sheetlist, form=form)

@sheetmod.route('/view_sheet2/', methods=['GET', 'POST'])
@login_required
def view_sheet2():
    selected_sheet_id = request.args['selected_sheet']
    sheet_title=Sheet.query.filter_by(id=selected_sheet_id).first().title
    sheetposts = SheetPost.query.filter_by(sheet_id=selected_sheet_id).all()
    postid_list=[]
    for item in sheetposts:
        postid_list.append(item.post_id)
    my_selected_postlist = Post.query.filter(Post.id.in_(postid_list)).order_by(Post.level).all()
    return render_template('sheets/view_sheet2.html',postlist=my_selected_postlist, sheet_title=sheet_title)