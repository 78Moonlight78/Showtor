import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm
from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Rating(SqlAlchemyBase, UserMixin):
    __tablename__ = 'ratings'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    cinema_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("cinemas.id"))
    rating = sqlalchemy.Column(sqlalchemy.Float)

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    # jobs = orm.relation("Job", back_populates='user')