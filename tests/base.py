"""
    Contains common classes used in various test scenarios.
"""
import warnings

from faker import Faker
from flask_testing import TestCase

from project import create_app, db
from manage import _generate_hash_algorithms, _generate_matrices, _commit


class BaseTestCase(TestCase):
    """
        This class contains the basic `setUp` and `tearDown` actions that must be performed before
    and after each test scenario is executed.
    """

    def create_app(self):
        warnings.filterwarnings('ignore', category=DeprecationWarning)
        return create_app(settings='project.config.TestingConfig')

    def setUp(self):
        db.create_all()

        _generate_hash_algorithms()
        _generate_matrices()
        _commit()

        self.fake = Faker()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
