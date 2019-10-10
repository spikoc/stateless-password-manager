"""
    Test views of the 'matrix' blueprint.
"""
# pylint: disable=no-member
from tests import BaseTestCase
from project.matrix.models import Matrix


class MatrixBlueprintTest(BaseTestCase):
    """Test functionality of the 'matrix' blueprint"""

    def test_add_page(self):
        """test adding a new :class:`project.matrix.models.Matrix` object"""
        form = {'name': self.fake.company(), 'algorithm_id': 4, 'salt': self.fake.md5()}
        response = self.client.post('/matrix/add', data=form, follow_redirects=True)

        self.assertEqual(200, response.status_code)
        self.assertIn('New matrix was created.', str(response.data))

        # .............................test database entry exists
        self.assertIsInstance(Matrix.query.filter_by(name=form['name']).first(), Matrix)

    def test_edit_page(self):
        """test editing an existing :class:`project.matrix.models.Matrix` object"""
        model = Matrix.query.first()
        form = {
            'name': '{0.name}_edited'.format(model),
            'algorithm_id': model.algorithm_id,
            'salt': model.salt,
            'length': model.length + 8
        }

        response = self.client.post('/matrix/edit/{0.id}'.format(model), data=form,
                                    follow_redirects=True)

        self.assertEqual(200, response.status_code)
        self.assertIn("Matrix was updated successfully.", str(response.data))

        # .............................test database entry is updated
        self.assertEqual(model.name, Matrix.query.filter_by(id=model.id).first().name)
        self.assertEqual(model.length, Matrix.query.filter_by(id=model.id).first().length)

    def test_index_page(self):
        """TODO: add method docstring"""
        response = self.client.get('/matrix/')

        self.assertEqual(200, response.status_code)
