from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.users.models import User
from app.posts.models import Post
from app. topics.models import Topic

class TopicForm(FlaskForm):
    topic=StringField('Thema', validators=[DataRequired()])
    submit=SubmitField('Post')