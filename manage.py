#!/usr/bin/env python
"""
    TODO: add module docstring
"""
from flask.cli import FlaskGroup

from project import create_app

APP = create_app()
CLI = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    CLI()
