"""
    Implements a WSGI application that acts as the central object.
"""
# pylint: disable=invalid-name

import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()
toolbar = DebugToolbarExtension()


def create_app(**kwargs):
    """
        Create a new WSGI application, register blueprints and initialize extensions.

    :key name    : The name of the Flask application.
    :key settings: The object with that name will be imported to set environment variables.
    """
    app = Flask(kwargs.pop('name', os.getenv('APP_NAME', __name__)))

    # .................................set configuration
    app.config.from_object(kwargs.pop(
        'settings', os.getenv('APP_SETTINGS', 'project.config.DevelopmentConfig')))

    # .................................set up extensions
    bootstrap.init_app(app)
    db.init_app(app)
    toolbar.init_app(app)

    # .................................register blueprints
    from project.main.views import main_blueprint
    from project.matrix.views import matrix_blueprint
    from project.evaluate.views import  evaluate_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(matrix_blueprint)
    app.register_blueprint(evaluate_blueprint)

    return app
