import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, validators
from wtforms.validators import DataRequired, Regexp, Length, ValidationError


def No_cyrillic(form, field): # Не работает
    # Регулярное выражение для проверки наличия кириллических символов
    if re.search('[а-яА-Я]', field.data):
        raise ValidationError('Use only latins symbols')

class RedeployForm(FlaskForm):
    username = StringField('First and last name', validators=[
        DataRequired(),
        Length(min=5, max=50, message="Enter correct first and last name"),
        No_cyrillic # Не работает
    ])

    email = EmailField('Email', [validators.DataRequired(), validators.Email()])
    submit = SubmitField('Redeploy')
