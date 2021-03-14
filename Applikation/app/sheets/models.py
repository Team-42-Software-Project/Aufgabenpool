from app import db
from datetime import datetime 

class Sheet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title= db.Column(db.String(100), nullable=False, default='N/A')
    topic =db.Column(db.String(200), nullable=False, default='N/A')
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
#sheetposts=db.relationship('SheetPost', backref='sheetX', lazy=True)
    
    def __repr__(self):
        return 'Aufgabenblatt  '

class SheetPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id =db.Column(db.Integer)
    sheet_id =db.Column(db.Integer)

    def __repr__(self):
        return 'Aufgabenblattaufgabe  '