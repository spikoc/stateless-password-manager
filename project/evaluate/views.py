"""
    TODO: add module docstring
"""

from flask import Blueprint, redirect, render_template,request, url_for
from project.evaluate.forms import EvaluateForm

evaluate_blueprint = Blueprint('evaluate', __name__, url_prefix='/evaluate')


@evaluate_blueprint.route('/', methods=['GET', 'POST'])
def index():

    form = EvaluateForm(request.form)
    if form.validate_on_submit():
        print("ok")

        return redirect(url_for('matrix.index'))
    return render_template('evaluate/index.html', form=form)
