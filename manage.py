#!/usr/bin/env python
"""
    TODO: add module docstring
"""
# pylint: disable=invalid-name
# pylint: disable=no-member

import sys
import time
import unittest

from datetime import datetime

from coverage import coverage
from flask.cli import FlaskGroup

from project import create_app, db

# app = create_app()
cli = FlaskGroup(create_app=create_app)
cov = coverage(branch=True, include='project/*', omit=[
    'project/config.py',
    'project/__init__.py',
    'project/*/__init__.py'
])
cov.start()


def _commit():
    """Commit record changes - rollback in case of error."""
    try:
        db.session.commit()

    except Exception as err:
        print(err.__class__.__name__, err)
        db.session.rollback()


def _execute_unittests():
    """Run the unittests."""
    try:
        tests = unittest.TestLoader().discover('tests')
        result = unittest.TextTestRunner(verbosity=2).run(tests)

        assert result.wasSuccessful()

    except AssertionError:
        sys.exit(1)

    finally:
        cov.stop()
        cov.save()


def _generate_hash_algorithms():
    """Generate hash algorithm data samples."""
    from project.matrix.models import Algorithm

    models = [
        Algorithm(name='md5'),
        Algorithm(name='sha1'),
        Algorithm(name='sha224'),
        Algorithm(name='sha256'),
        Algorithm(name='sha384'),
        Algorithm(name='sha512')
    ]

    for model in models:
        print(model)
        db.session.add(model)


def _generate_matrices():
    """Generate matrix data samples."""
    from project.matrix.models import Matrix

    models = [
        Matrix(name='Gmail', algorithm_id=4, salt='fd70e5b3b577a1572436847b8e65875e',
               created_at=datetime.now(), modified_at=datetime.now()),
        Matrix(name='Facebook', algorithm_id=6, salt='60a8ec4be6ab4b909ea811a18156781c',
               iterations=2048, created_at=datetime.now(), modified_at=datetime.now()),
        Matrix(name='Instagram', algorithm_id=1, salt='a1791e97739c206a7bb09ddff3ecb51d',
               iterations=512, length=8, created_at=datetime.now(), modified_at=datetime.now()),
        Matrix(name='LinkedIn', algorithm_id=2, salt='0e9c6984dfc3ad02827f0c67288b0bc5',
               iterations=4096, length=32, created_at=datetime.now(), modified_at=datetime.now()),
        Matrix(name='Codecademy', algorithm_id=5, salt='a7c331d5c1a75b0894871da345ac05db',
               iterations=4096, length=12, created_at=datetime.now(), modified_at=datetime.now()),
        Matrix(name='Slack', algorithm_id=3, salt='5d7549459403b55798c3e713facfeea4',
               iterations=128, created_at=datetime.now(), modified_at=datetime.now())
    ]

    for model in models:
        print(model)
        db.session.add(model)


@cli.command()
def generate_sample_data():
    """Feed the database with sample data."""
    _generate_hash_algorithms()
    _generate_matrices()
    _commit()


@cli.command()
def init_db():
    """Clear the database and create a new schema."""
    print('[*] Drops all tables...')
    db.drop_all()

    print('[*] Creates all tables, again...')
    db.create_all()

    print('DONE')


@cli.command()
def test():
    """Run the unittests without coverage."""
    _execute_unittests()


@cli.command()
def test_with_coverage():
    """Run the unittests with coverage."""
    _execute_unittests()
    time.sleep(1)  # ..................avoid collapse

    print('Coverage Summary:')
    cov.report()
    cov.html_report()
    cov.erase()


if __name__ == '__main__':
    cli()
