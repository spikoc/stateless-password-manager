"""
    Implements a WSGI application that acts as the central object.
"""
import os

from flask import Flask


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

    # .................................register blueprints
    from project.main.views import main_blueprint

    app.register_blueprint(main_blueprint)

    return app
