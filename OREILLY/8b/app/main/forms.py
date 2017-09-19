from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

# 这里只有一个表单，如果表单太多，写成单独的文件更清晰直观
class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')
