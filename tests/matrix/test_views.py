"""
    TODO: add module docstring
"""
# pylint: disable=no-member
from tests import BaseTestCase
from project.matrix.models import Matrix


class MatrixBlueprintTest(BaseTestCase):
    """TODO: add class docstring"""

    def test_add_page(self):
        """test adding a new :class:`project.matrix.models.Matrix` object"""
        form = {'name': self.fake.company(), 'algorithm_id': 4, 'salt': self.fake.md5()}
        response = self.client.post('/matrix/add', data=form, follow_redirects=True)

        self.assertEqual(200, response.status_code)
        self.assertIn('New matrix was created.', str(response.data))

        # .............................test database entry exists
        self.assertIsInstance(Matrix.query.filter_by(name=form['name']).first(), Matrix)

    def test_index_page(self):
        """TODO: add method docstring"""
        response = self.client.get('/matrix/')

        self.assertEqual(200, response.status_code)
