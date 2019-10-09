"""
    TODO: add module docstring
"""

from flask import Blueprint, redirect, render_template,request, url_for

evaluate_blueprint = Blueprint('evaluate', __name__, url_prefix='/evaluate')


@evaluate_blueprint.route('/')
def index():
    """"""
    return "hello"