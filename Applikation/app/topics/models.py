from datetime import datetime 
from app import db, login_manager
from flask_login import UserMixin



class Topic(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return 'Thema  '( + str(self.id))