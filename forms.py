from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class CodeForm(FlaskForm):
    Code = StringField()
    Submit = SubmitField()