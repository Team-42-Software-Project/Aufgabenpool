from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, FieldList
from wtforms.validators import DataRequired  


class SheetForm(FlaskForm):
    title=StringField('Titel des Arbeitsblattes', validators=[DataRequired()])
    submit=SubmitField('Speichern')

class SelectTopicForm(FlaskForm):
    topic=StringField('Thema', validators=[DataRequired()])
    submit=SubmitField('Auswählen')

class SelectSheetForm(FlaskForm):
    id =IntegerField('Arbeitsblatt-ID', validators=[DataRequired()])
    submit=SubmitField('Herunterladen')

class SelectSheetViewForm(FlaskForm):
    id =IntegerField('Arbeitsblatt-ID', validators=[DataRequired()])
    submit=SubmitField('Ansehen')
