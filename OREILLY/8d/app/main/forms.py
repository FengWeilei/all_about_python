from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# 这里暂时都用不上了。
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
