
import os
import secrets
from PIL import Image
from flask import render_template, request, redirect, url_for, flash, abort
from app import app, db, bcrypt 
from app.forms import RegistrationForm, LoginForm, UpdateAccountForm, PostForm
from app.models import User, Aufgabe
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def home2():
   
    return render_template('home2.html')


@app.route('/register', methods=['GET', 'POST'] )
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home2'))

    form=RegistrationForm()
    if form.validate_on_submit():
            hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            user=User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            flash(f'Account wurde gemacht, Sie können sich einloggen', 'success')
            return redirect(url_for('login')) 

    return render_template('register.html', form=form)




@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home2'))

    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page= request.args.get('next')
            flash(f'Sie sind eingeloggt', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home2'))
        else:
            flash(f'Ckeck email and password!', 'danger') 

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


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

@app.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form=UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file= save_picture(form.picture.data)
            current_user.image_file=picture_file
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Account wurde updatet', 'success')
        return redirect(url_for('account'))
    elif request.method== 'GET':
        form.username.data=current_user.username
        form.email.data=current_user.email

    image_file=url_for('static', filename='profile_pics/'+ current_user.image_file)
    return render_template('account.html', title='Account', image_file=image_file, form=form)

@app.route('/users/')
def users():   
       users= User.query.all()
       return render_template('users.html', users=users)
       

@app.route('/eingabe/')
def eingabe():   
       posts= Aufgabe.query.all()
       return render_template('eingabe.html', posts=posts)


@app.route('/eingabe/<int:post_id>')
def post(post_id):   
       post= Aufgabe.query.get_or_404(post_id)     
       return render_template('post.html', post=post)


@app.route('/eingabe/edit/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit(post_id):
    post= Aufgabe.query.get_or_404(post_id)
    if post.autor != current_user:
        abort(403)
    form=PostForm()
    if form.validate_on_submit():
        post.fach=form.fach.data
        post.thema=  form.thema.data
        post.level= form.level.data
        post.aufgabe=  form.aufgabe.data
        db.session.commit()
        flash('Aufgabe wurde updatet', 'success')
        return redirect(url_for('eingabe', post_id=post.id))
    elif request.method=='GET':
        form.fach.data= post.fach
        form.thema.data= post.thema
        form.level.data= post.level
        form.aufgabe.data= post.aufgabe
    return render_template('new_post2.html', title= 'Update Aufgabe', form=form, legend='Update Aufgabe')

  

@app.route('/new/', methods=['GET', 'POST'])
@login_required
def new_post():
    form =PostForm()
    if form.validate_on_submit():
        post= Aufgabe(fach=form.fach.data, thema= form.thema.data, level=form.level.data, 
        aufgabe=form.aufgabe.data, autor=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Aufgabe wurde erstellt', 'success')
        return redirect(url_for('eingabe'))
    
    return render_template('new_post2.html', title= 'Neue Aufgabe', form=form, legend='Neue Aufgabe')




@app.route('/eingabe/delete/<int:post_id>', methods=['POST'] )
@login_required
def delete(post_id):
    post= Aufgabe.query.get_or_404(post_id)
    if post.autor != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Aufgabe wurde gelöscht', 'success')
    return redirect('/eingabe/')




@app.route('/aufgaben/', methods=[ 'GET','POST'])
def get_req():
    return render_template('aufgaben.html')


@app.route('/email/', methods=[ 'GET','POST'])
def email():
    return render_template('email.html')

 