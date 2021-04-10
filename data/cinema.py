import datetime
import sqlalchemy
from flask_login import UserMixin

from sqlalchemy import orm

from werkzeug.security import generate_password_hash, check_password_hash

from .db_session import SqlAlchemyBase


class Cinema(SqlAlchemyBase):
    __tablename__ = 'cinemas'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("cinema_types.id"))
    genres = sqlalchemy.Column(sqlalchemy.ARRAY, sqlalchemy.ForeignKey("genres.id"))
    name = sqlalchemy.Column(sqlalchemy.String)
    duration = sqlalchemy.Column(sqlalchemy.Integer) # в секундах (одна серия)
    age_category = sqlalchemy.Column(sqlalchemy.Integer)
    cover_art = sqlalchemy.Column(sqlalchemy.LargeBinary) # обложка
    description = sqlalchemy.Column(sqlalchemy.String)
    bundles = sqlalchemy.Column(sqlalchemy.String) # связка с другими фильмами/сериалами
    release_date = sqlalchemy.Column(sqlalchemy.DATE)

    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)



    # jobs = orm.relation("Job", back_populates='user')
    """
    team_leader_id = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    """
