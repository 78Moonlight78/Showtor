import datetime
import sqlalchemy

from .db_session import SqlAlchemyBase


class UserNet(SqlAlchemyBase):
    """
    Класс, описывающий сети(месенджеры, социальные сети) которые использует пользователь
    """
    __tablename__ = 'users_nets'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))  # id пользователя, к которому привязан ключ
    net_name = sqlalchemy.Column(sqlalchemy.String)  # название сети, для которой используеться ключ
    net_ident = sqlalchemy.Column(sqlalchemy.String)  # ключ, для данной сети

    last_use = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)  # время послоеднего обращения к пользователю, по данному ключу

    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    is_visible = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
