"""
    TODO: add module docstring
"""
from project import db


class Algorithm(db.Model):
    """State the columns that describe a hash algorithm model."""

    __tablename__ = 'algorithm'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(8), nullable=False)

    def __repr__(self):
        return "<{}(id={}, name='{}')>".format(self.__class__.__name__, self.id, self.name)


class Matrix(db.Model):
    """State the columns that describe a matrix model."""

    __tablename__ = 'matrix'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    algorithm_id = db.Column(db.Integer, db.ForeignKey('algorithm.id'))
    salt = db.Column(db.String(32), nullable=False)
    iterations = db.Column(db.Integer, nullable=False, default=1024)
    length = db.Column(db.Integer, nullable=False, default=8)
    created_at = db.Column(db.DateTime, nullable=False)
    modified_at = db.Column(db.DateTime, nullable=False)

    algorithm = db.relationship('Algorithm', foreign_keys='Matrix.algorithm_id')

    def __repr__(self):
        return "<{}(id={}, name='{}')>".format(self.__class__.__name__, self.id, self.name)
