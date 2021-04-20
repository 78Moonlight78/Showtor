import sqlalchemy
from .db_session import SqlAlchemyBase


class CinemaType(SqlAlchemyBase):
    """
    типы фильмов(фильм, сериал, мультфильм)
    """
    __tablename__ = 'cinema_types'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)  # название типа

    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)