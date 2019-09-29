"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

from hashlib import pbkdf2_hmac

from binascii import hexlify
from flask import Blueprint, redirect, render_template, request, url_for

from project.matrix.forms import EditForm
from project.matrix.models import Matrix

matrix_blueprint = Blueprint('matrix', __name__, url_prefix='/matrix')


@matrix_blueprint.route('/')
def index():
    """TODO: add function docstring"""
    return render_template('matrix/index.html', items=Matrix.query.all())


@matrix_blueprint.route('/add')
def add():
    """TODO: add function docstring"""
    return render_template('matrix/edit.html')


@matrix_blueprint.route('/delete')
def delete():
    """TODO: add function docstring"""
    return render_template('matrix/index.html')


@matrix_blueprint.route('/edit/<int:matrix_id>', methods=['GET', 'POST'])
def edit(matrix_id):
    """TODO: add function docstring"""
    form = EditForm(request.form)
    if form.validate_on_submit():
        print(
            hexlify(
                pbkdf2_hmac(
                    form.algorithm.data.strip(),
                    'password'.encode('utf-8'),
                    form.salt.data.strip().encode('utf-8'),
                    form.iterations.data,
                    dklen=form.length.data if form.length.data else None
                )
            )
        )

        return redirect(url_for('matrix.index'))

    # TODO: ensure record with given id exists
    return render_template(
        'matrix/edit.html', form=form, model=Matrix.query.filter_by(id=matrix_id).first())


@matrix_blueprint.route('/view')
def view():
    """TODO: add function docstring"""
    return render_template('matrix/view.html')
