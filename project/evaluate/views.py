"""
    TODO: add module docstring
"""

from flask import Blueprint, redirect, render_template,request, url_for
from project.evaluate.forms import EvaluateForm

evaluate_blueprint = Blueprint('evaluate', __name__, url_prefix='/evaluate')


@evaluate_blueprint.route('/', methods=['GET', 'POST'])
def index():

    power = None
    form = EvaluateForm(request.form)
    if form.validate_on_submit():
        print(form.password.data)
        if form.password.data != None and form.password.data != '':
            power = 'Weak Password'

        return render_template('evaluate/index.html', form=form, power=power)

    return render_template('evaluate/index.html', form=form)
