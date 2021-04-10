import datetime
import sqlalchemy
from flask_login import UserMixin

from sqlalchemy import orm

from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Genre(SqlAlchemyBase):
    __tablename__ = 'genres'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)