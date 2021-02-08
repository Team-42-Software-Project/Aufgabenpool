
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///aufgabe.db'
db=SQLAlchemy(app)


class Aufgabe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fach= db.Column(db.String(100), nullable=False)
    thema =db.Column(db.String(100), nullable=False)
    aufgabe =db.Column(db.Text,nullable=False)
    author=db.Column(db.String(20), nullable=False, default='N/A')
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Aufgabe  ' + str(self.id)



@app.route('/')
def index():
    return render_template('index.html')


@app.route('/eingabe/', methods=['GET','POST'])
def posts():
    
        all_posts=Aufgabe.query.order_by(Aufgabe.date_posted).all()
        return render_template('eingabe.html', posts=all_posts)


@app.route('/eingabe/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    post= Aufgabe.query.get_or_404(id)

    if request.method=='POST':
        post.fach= request.form['fach']
        post.thema= request.form['thema']
        post.aufgabe= request.form['aufgabe']
        post.author= request.form['author']
        db.session.commit()

        return redirect('/eingabe/')
    else: 
        return render_template('edit.html', post=post)

  
@app.route('/new/', methods=['GET', 'POST'])
def new_post():
    
    if request.method=='POST':
        post_fach= request.form['fach']
        post_thema= request.form['thema']
        post_aufgabe= request.form['aufgabe']
        post_author= request.form['author']
        new_post =Aufgabe(fach=post_fach,thema=post_thema, aufgabe= post_aufgabe, author=post_author)
        
        db.session.add(new_post)
        db.session.commit()

        return redirect('/new/')
    else: 
        return render_template('new_post.html')


#

@app.route('/eingabe/delete/<int:id>')
def delete (id):
    post= Aufgabe.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/eingabe/')



@app.route('/home/<string:name>')
def hello(name):
    return "hello  " +name

@app.route('/aufgaben/', methods=[ 'GET','POST'])
def get_req():
    return render_template('aufgaben.html')


@app.route('/email/', methods=[ 'GET','POST'])
def email():
    return render_template('email.html')

 




if __name__== "__main__":
    app.run(debug=True)


