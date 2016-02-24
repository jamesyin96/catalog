from flask_wtf import Form
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired


class MyForm(Form):
    name = StringField('name', validators=[DataRequired()])
    description = TextAreaField('description', validators=[DataRequired()])
    category = SelectField('category')
    upload = FileField('image',
                       validators=[FileAllowed(['jpg', 'png'],
                                   'Images only!')])
