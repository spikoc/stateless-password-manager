#!/usr/bin/env python
"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

from flask.cli import FlaskGroup

from project import create_app

app = create_app()
cli = FlaskGroup(create_app=create_app)


if __name__ == '__main__':
    cli()
