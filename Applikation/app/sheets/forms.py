from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired  


class SheetForm(FlaskForm):
    subject=StringField('Fach', validators=[DataRequired()])
    topic=StringField('Thema', validators=[DataRequired()])
    level=IntegerField('Level', validators=[DataRequired()])
    text=TextAreaField('Aufgabentext', validators=[DataRequired()])
    submit=SubmitField('Speichern')

class SelectTopicForm(FlaskForm):
    topic=StringField('Thema', validators=[DataRequired()])
    submit=SubmitField('Speichern2')