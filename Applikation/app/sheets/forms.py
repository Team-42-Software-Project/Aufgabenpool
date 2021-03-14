from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FieldList
from wtforms.validators import DataRequired  


class SheetForm(FlaskForm):
    title=StringField('Titel des Arbeitsblattes', validators=[DataRequired()])
    #topic=StringField('Thema', validators=[DataRequired()])
   # post_ids = FieldList(IntegerField)
    submit=SubmitField('Speichern')

class SelectTopicForm(FlaskForm):
    topic=StringField('Thema', validators=[DataRequired()])
    submit=SubmitField('Speichern')