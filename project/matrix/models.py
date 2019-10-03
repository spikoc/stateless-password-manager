"""
    TODO: add module docstring
"""
from project import db


class Matrix(db.Model):
    """State the columns that describe a matrix model."""

    __tablename__ = 'matrix'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    algorithm = db.Column(db.String(16), nullable=False)
    salt = db.Column(db.String(32), nullable=False)
    iterations = db.Column(db.Integer, nullable=False, default=1024)
    length = db.Column(db.Integer, nullable=False, default=8)
    created_at = db.Column(db.Date, nullable=False)
    modified_at = db.Column(db.Date, nullable=False)
