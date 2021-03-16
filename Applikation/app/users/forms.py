from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.users.models import User

class RegistrationForm(FlaskForm):
    username= StringField('Username', validators=[DataRequired(), Length(min=1, max=30)])
    email=StringField ('Email', validators=[DataRequired(), Email()]) 
    password=PasswordField('Password', validators=[DataRequired()])
    confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    image_file = FileField('Image_File', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit=SubmitField('Sign in')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('That username is taken')

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('That email is taken')


class LoginForm(FlaskForm):
    email=StringField ('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')


