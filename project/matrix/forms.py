"""
    TODO: add module docstring
"""
from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField, StringField


class EditForm(FlaskForm):
    """TODO: add class docstring"""

    name = StringField('Name', description='Name of the matrix')
    algorithm = StringField('Algorithm', description='Select the hash digest algorithm')
    salt = StringField('Salt', description='Salts make the search space larger in the case of '
                                           'brute forcing')
    uppercase = BooleanField('Contains uppercase letters')
    lowercase = BooleanField('Contains lowercase letters')
    digits = BooleanField('Contains digits')
    symbols = BooleanField('Contains symbols')
    iterations = IntegerField('Iterations', description='Number or iterations in calculation '
                                                        '(higher means more computation required)')
    length = IntegerField('Length', description='length of the output password (not required)')
