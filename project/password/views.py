"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

from flask import Blueprint, render_template

password_blueprint = Blueprint('password', __name__, url_prefix='/password')


@password_blueprint.route('/')
def index():
    """TODO: add function docstring"""
    return render_template('password/index.html')


@password_blueprint.route('/add')
def add():
    """TODO: add function docstring"""
    return render_template('password/edit.html')


@password_blueprint.route('/delete')
def delete():
    """TODO: add function docstring"""
    return render_template('password/index.html')


@password_blueprint.route('/edit')
def edit():
    """TODO: add function docstring"""
    return render_template('password/edit.html')


@password_blueprint.route('/view')
def view():
    """TODO: add function docstring"""
    return render_template('password/view.html')
