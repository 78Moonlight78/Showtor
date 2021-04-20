import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase


class Rating(SqlAlchemyBase):
    __tablename__ = 'ratings'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))  # пользоваетль, создавший оценку
    cinema_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("cinemas.id"))  # фильм, о котором сделлан оценка
    rating = sqlalchemy.Column(sqlalchemy.Float)  # оценка пользоваетля
    is_rating = sqlalchemy.Column(sqlalchemy.Boolean)  # являеться ли оценка рейтпингом, или это что-то, что понравилось/не понравилось пользователю

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)