"""
    TODO: add module docstring
"""
from flask_testing import TestCase

from project import create_app


class EvaluateBlueprintTest(TestCase):
    """TODO: add class docstring"""

    def create_app(self):
        return create_app(settings='project.config.TestingConfig')

    def test_index_page(self):
        """TODO: add method docstring"""
        response = self.client.get('/evaluate')

        self.assertEqual(200, response.status_code)
        self.assertIn('Password', str(response.data))
