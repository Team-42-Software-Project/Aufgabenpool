
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts2.db'
db=SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =db.Column(db.String(20), unique=True,nullable=False )
    email =db.Column(db.String(120), unique=True,nullable=False )
    image_file=db.Column(db.String(20),nullable=False, default='default.jpg' )
    passwort= db.Column(db.String(60),nullable=False )
    posts= db.relationship('Post', backref='author', lazy=True)



    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titel =db.Column(db.String(1000),nullable=False )
    date_posted=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content =db.Column(db.Text,nullable=False )
    user_id= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.titel}','{self.date_posted}')"



all_posts =[
    { 
    'title':'Post 1',
    'content':'This is content post 1',
    'author': 'Aaron'},

    {
        'title':'Post 2',
    'content':'This is content post2'}
]


@app.route('/')
def index():
    return render_template('index.html')




@app.route('/home/<string:name>')
def hello(name):
    return "hello  " +name

@app.route('/onlyget', methods=[ 'GET','POST'])
def get_req():
    return "You can only get this"



    
if __name__== "__main__":
    app.run(debug=True)


