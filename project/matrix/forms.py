"""
    TODO: add module docstring
"""
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField


class EditForm(FlaskForm):
    """TODO: add class docstring"""

    name = StringField('name')
    algorithm = StringField('hash digest algorithm')
    salt = StringField('salt')
    iterations = IntegerField('number of iterations')
    uppercase = BooleanField('uppercase letters')
    lowercase = BooleanField('lowercase letters')
    digits = BooleanField('digits')
    symbols = BooleanField('symbols')
    length = IntegerField('length of password')
