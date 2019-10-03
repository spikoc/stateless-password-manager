#!/usr/bin/env python
"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name

import sys
import time
import unittest

from coverage import coverage
from flask.cli import FlaskGroup

from project import create_app

# app = create_app()
cli = FlaskGroup(create_app=create_app)
cov = coverage(branch=True, include='project/*', omit=[
    'project/config.py',
    'project/__init__.py',
    'project/*/__init__.py'
])
cov.start()


@cli.command()
def run_coverage():
    """Run the unit tests with coverage."""
    try:
        tests = unittest.TestLoader().discover('tests')
        result = unittest.TextTestRunner(verbosity=2).run(tests)

        assert result.wasSuccessful()

    except AssertionError:
        sys.exit(1)

    finally:
        cov.stop()
        cov.save()

    time.sleep(1)  # ..................avoid collapse
    print('Coverage Summary:')

    cov.report()
    cov.html_report()
    cov.erase()


if __name__ == '__main__':
    cli()
