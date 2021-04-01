from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired  


class PostForm(FlaskForm):
    subject=StringField('Fach', validators=[DataRequired()])
    topic=StringField('Thema', validators=[DataRequired()])
    level=IntegerField('Level', validators=[DataRequired()])
    text=TextAreaField('Aufgabentext', validators=[DataRequired()])
    submit=SubmitField('Speichern')