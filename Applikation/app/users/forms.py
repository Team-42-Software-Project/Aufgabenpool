from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.users.models import User

class RegistrationForm(FlaskForm):
    username= StringField('Nutzername', validators=[DataRequired(), Length(min=1, max=30)])
    email=StringField ('E-Mail-Adresse', validators=[DataRequired(), Email()]) 
    password=PasswordField('Passwort', validators=[DataRequired()])
    confirm_password=PasswordField('Passwort erneut eingeben', validators=[DataRequired(), EqualTo('password')])
    image_file = FileField('Profilbild', validators=[
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])
    submit=SubmitField('Registrieren')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError('Dieser Nutzername wurde schon verwendet')

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Diese E-Mail-Adresse wurde schon verwendet')


class LoginForm(FlaskForm):
    email=StringField ('E-Mail-Adresse', validators=[DataRequired(), Email()])
    password=PasswordField('Passwort', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Login')


