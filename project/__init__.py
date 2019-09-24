"""
    Implements a WSGI application that acts as the central object.
"""
from flask import Flask


def create_app(**kwargs):
    """Create a new WSGI application, register blueprints and initialize extensions."""
    app = Flask(kwargs.pop('name', __name__))

    # .................................register blueprints
    from project.main.views import main_blueprint

    app.register_blueprint(main_blueprint)

    return app
