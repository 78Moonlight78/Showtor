import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users_nets'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    favourite_cinema_types = sqlalchemy.Column(sqlalchemy.ARRAY, sqlalchemy.ForeignKey("cinema_types.id"))
    favourite_genres = sqlalchemy.Column(sqlalchemy.ARRAY, sqlalchemy.ForeignKey("genres.id"))

    user_plan = sqlalchemy.Column(sqlalchemy.ARRAY)
    user_viewed = sqlalchemy.Column(sqlalchemy.ARRAY)

    age = sqlalchemy.Column(sqlalchemy.Integer)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    age = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    position = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    speciality = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
