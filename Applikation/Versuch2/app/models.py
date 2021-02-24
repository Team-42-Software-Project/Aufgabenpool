
from datetime import datetime 
from app import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    image_file=db.Column(db.String(20), nullable=False, default='default.jpg')
    password=db.Column(db.String(60), nullable=False)
    posts=db.relationship('Aufgabe', backref='autor', lazy=True)


    def __repr__(self):
        return f"User ('{self.username}','{self.email}','{self.image_file}')"

        
class Aufgabe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fach= db.Column(db.String(100), nullable=False, default='N/A')
    thema =db.Column(db.String(100), nullable=False, default='N/A')
    aufgabe =db.Column(db.Text,nullable=True, default='N/A')
    level=db.Column(db.Integer, nullable=True, default='N/A')
    date_posted=db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Aufgabe  '( + str(self.id)+ str(self.fach)+ str(self.thema))

class Thema(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    thema =db.Column(db.String(100), nullable=False, default='N/A')
    date_posted=db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Thema  '( + str(self.id)+ str(self.thema))

