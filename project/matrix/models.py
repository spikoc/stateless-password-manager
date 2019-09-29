"""
    TODO: add module docstring
"""
from project import db


class Matrix(db.Model):
    """TODO: add class docstring"""

    __tablename__ = 'matrix'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    algorithm = db.Column(db.String(16), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    iterations = db.Column(db.Integer, nullable=False)
    length = db.Column(db.Integer)
