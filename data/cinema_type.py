import datetime
import sqlalchemy
from flask_login import UserMixin

from sqlalchemy import orm

from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class CinemaType(SqlAlchemyBase):
    __tablename__ = 'cinema_types'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)