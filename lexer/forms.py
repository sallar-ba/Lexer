from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import InputRequired

class CodeForm(FlaskForm):
    code = TextAreaField('Code', validators=[InputRequired()], render_kw={"placeholder": "Enter Code..."})
    submit = SubmitField('Submit', render_kw={"class": "btn btn-primary"})


# class TreeForm(FlaskForm):
#     expression = StringField('Expression', validators=[InputRequired()], render_kw={"placeholder": "Enter Expression..."})
#     submit = SubmitField('Generate', render_kw={"class": "btn btn-primary"})