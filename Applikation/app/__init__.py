
from flask import Flask
from flask_sqlalchemy import SQLAlchemy





app = Flask(__name__)
app.config['SECRET_KEY']='ecae627829ff8e6a39cc4c285c024e29'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datenbank.db'
db=SQLAlchemy(app)

from app import views
