"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

from flask import Blueprint

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    """TODO: add function docstring"""
    return "stateless-password-manager"
