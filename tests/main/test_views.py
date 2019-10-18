"""
    Test views of the 'main' blueprint.
"""
from tests import BaseTestCase


class MainBlueprintTest(BaseTestCase):
    """Test functionality of the 'main' blueprint."""

    def test_index_page(self):
        """test that home page is accessible"""
        response = self.client.get('/')

        self.assertEqual(200, response.status_code)
        self.assertIn('Hello Friend.', str(response.data))
