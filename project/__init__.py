"""
    Implements a WSGI application that acts as the central object.
"""
# pylint: disable=invalid-name
# pylint: disable=unused-variable

import os

from flask import Flask, render_template
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

    app.register_blueprint(main_blueprint)
    app.register_blueprint(matrix_blueprint)

    @app.errorhandler(404)
    def page_not_found(error):
        """Redirect to a custom page when the return status code is 404."""
        print(error)
        return render_template('errors/page_not_found.html'), 404

    return app
