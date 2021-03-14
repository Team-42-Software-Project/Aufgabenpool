
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SECRET_KEY']='ecae627829ff8e6a39cc4c285c024e29'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///datenbank.db'
db=SQLAlchemy(app)

bcrypt= Bcrypt(app)
login_manager= LoginManager(app)
login_manager.login_view= 'login'
login_manager.login_message_category='info'


from app import views

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)
from app.posts.views import postmod as postsModule
app.register_blueprint(postsModule)
from app.topics.views import topicmod as topicsModule
app.register_blueprint(topicsModule)
from app.sheets.views import sheetmod as sheetsModule
app.register_blueprint(sheetsModule)



