"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

from flask import Blueprint, redirect, render_template, request, url_for

from project.matrix.forms import EditForm

matrix_blueprint = Blueprint('matrix', __name__, url_prefix='/matrix')


@matrix_blueprint.route('/')
def index():
    """TODO: add function docstring"""
    return render_template('matrix/index.html')


@matrix_blueprint.route('/add')
def add():
    """TODO: add function docstring"""
    return render_template('matrix/edit.html')


@matrix_blueprint.route('/delete')
def delete():
    """TODO: add function docstring"""
    return render_template('matrix/index.html')


@matrix_blueprint.route('/edit', methods=['GET', 'POST'])
def edit():
    """TODO: add function docstring"""
    form = EditForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('matrix.index'))

    return render_template('matrix/edit.html', form=form)


@matrix_blueprint.route('/view')
def view():
    """TODO: add function docstring"""
    return render_template('matrix/view.html')
