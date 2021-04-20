import sqlalchemy
from .db_session import SqlAlchemyBase


class Genre(SqlAlchemyBase):
    """
    жанры
    """
    __tablename__ = 'genres'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)  # название жанра
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)