import datetime
import sqlalchemy
from flask_login import UserMixin
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)

    favourite_cinema_types = sqlalchemy.Column(sqlalchemy.JSON, sqlalchemy.ForeignKey("cinema_types.id"))  # что предпочтительнее: фильм/сериал и т.д.
    favourite_genres = sqlalchemy.Column(sqlalchemy.JSON, sqlalchemy.ForeignKey("genres.id"))  # любимые жанры пользователя

    user_plan = sqlalchemy.Column(sqlalchemy.JSON)  # то, что пользователь хочет посмотреть, коментарии к этому
    #user_viewed = sqlalchemy.Column(sqlalchemy.JSON)  # то, что пользователь уже смотрел и оценка этх фильмов/сериалов, комментарии по ним

    age = sqlalchemy.Column(sqlalchemy.Integer) # возраст пользователя

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

    # hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # surname = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    # name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
