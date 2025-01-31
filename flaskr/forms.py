import re
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, validators
from wtforms.validators import DataRequired, Regexp, Length, ValidationError


'''
def no_cyrillic(self, username): # Не работает
    # Регулярное выражение для проверки наличия кириллических символов
    if re.search('[а-яА-Я]', username):
        raise ValidationError('Use only latins symbols'
'''

class RedeployForm(FlaskForm):
    username = StringField('First name and Last name:', validators=[
        DataRequired(),
        Length(min=5, max=50, message="Enter correct first and last name"),
        #no_cyrillic()
    ])

    email = EmailField('Email:', [
        validators.DataRequired(),
        validators.Email()
    ])
    def no_cyrillic(self, username):  # Не работает
        # Регулярное выражение для проверки наличия кириллических символов
        if re.search('[а-яА-Я]', username):
            raise ValidationError('Use only latins symbols')
    submit = SubmitField('Redeploy')