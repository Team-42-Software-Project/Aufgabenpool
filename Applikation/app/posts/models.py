from app import db
from datetime import datetime 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject= db.Column(db.String(100), nullable=False, default='N/A')
    topic =db.Column(db.String(100), nullable=False, default='N/A')
    text =db.Column(db.Text,nullable=True, default='N/A')
    level=db.Column(db.Integer, nullable=True, default='N/A')
    date_posted=db.Column(db.DateTime, nullable=True, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Aufgabe  '( + str(self.id)+ str(self.subject)+ str(self.topic))