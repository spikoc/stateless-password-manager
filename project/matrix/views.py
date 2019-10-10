"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

from hashlib import pbkdf2_hmac

from binascii import hexlify
from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for

from project import db
from project.matrix.forms import EditForm
from project.matrix.helpers import prepare_form_data
from project.matrix.models import Matrix

matrix_blueprint = Blueprint('matrix', __name__, url_prefix='/matrix')


@matrix_blueprint.route('/')
def index():
    """TODO: add function docstring"""
    return render_template('matrix/index.html', items=Matrix.query.all())


@matrix_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    """Add a new :class:`project.matrix.models.Matrix` object."""
    form = EditForm(request.form)

    if form.validate_on_submit():
        model = Matrix(created_at=datetime.now(), modified_at=datetime.now())
        form.populate_obj(model)

        db.session.add(model)
        db.session.commit()

        flash('New matrix was created.', 'success')
        return redirect(url_for('matrix.index'))

    return render_template('matrix/edit.html', form=prepare_form_data(form, Matrix(algorithm_id=0)))


@matrix_blueprint.route('/delete')
def delete():
    """TODO: add function docstring"""
    return render_template('matrix/index.html')


@matrix_blueprint.route('/edit/<int:matrix_id>', methods=['GET', 'POST'])
def edit(matrix_id):
    """Edit an existing :class:`project.matrix.models.Matrix` object."""
    model = Matrix.query.filter_by(id=matrix_id).first()
    assert model.id, "Matrix with '{0.id}' does not exist.".format(model)

    form = EditForm(request.form)

    if form.validate_on_submit():
        model.modified_at = datetime.now()
        form.populate_obj(model)

        db.session.commit()

        flash('Matrix was updated successfully.', 'success')
        return redirect(url_for('matrix.index'))

    return render_template('matrix/edit.html', form=prepare_form_data(form, model))


@matrix_blueprint.route('/view')
def view():
    """TODO: add function docstring"""
    return render_template('matrix/view.html')
