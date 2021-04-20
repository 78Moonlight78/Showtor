import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Cinema(SqlAlchemyBase):
    """
    инофрмация о фильме/сериале/мультфильме
    """
    __tablename__ = 'cinemas'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("cinema_types.id"))  # тип (фильм, сериал и т.д.)
    genres = sqlalchemy.Column(sqlalchemy.JSON, sqlalchemy.ForeignKey("genres.id"))  # жанры
    name = sqlalchemy.Column(sqlalchemy.String)  # название
    duration = sqlalchemy.Column(sqlalchemy.Integer)  # в секундах (одна серия)
    age_category = sqlalchemy.Column(sqlalchemy.Integer)  # возростное ограничение
    cover_art = sqlalchemy.Column(sqlalchemy.LargeBinary)  # обложка
    description = sqlalchemy.Column(sqlalchemy.String)  # описание
    bundles = sqlalchemy.Column(sqlalchemy.JSON)  # связка с другими фильмами/сериалами
    release_date = sqlalchemy.Column(sqlalchemy.DATE)  # дата релиза
    rating = sqlalchemy.Column(sqlalchemy.Float)    # рейтинг

    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
