"""
    TODO: add module docstring
"""
from flask_testing import TestCase

from project import create_app


class MainBlueprintTest(TestCase):
    """TODO: add class docstring"""

    def create_app(self):
        """Create the Flask application with the preferred settings to be tested."""
        app = create_app()
        app.config['TESTING'] = True

        return app

    def test_index_page(self):
        """TODO: add method docstring"""
        response = self.client.get('/')

        self.assertEqual(200, response.status_code)
        self.assertIn('Hello Friend.', str(response.data))
