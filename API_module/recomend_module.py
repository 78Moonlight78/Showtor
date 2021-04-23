from data import db_session
from data.user import User
from data.user_nets import UserNet
from data.cinema import Cinema
from data.cinema_type import CinemaType
from data.genre import Genre

from random import randint


def get_film_info(session, cinema_id):
    film = session.query(Cinema).filter(Cinema.id == cinema_id, Cinema.is_visible == True).first()

    cinema_type = session.query(CinemaType).filter(CinemaType.id == film.type, CinemaType.is_visible == True).first()
    if cinema_type is None:
        cinema_type = None
    else:
        cinema_type = cinema_type.name

    film_genres = [int(i) for i in film.genres.strip("[").strip("]").split(", ")]
    genres = session.query(Genre).filter(Genre.id.in_(film_genres), Genre.is_visible == True)
    genres_list = list()
    if genres is None:
        genres_list = None
    else:
        for i in genres:
            genres_list.append(i.name)

    out_data = {
        "film_name": film.name,
        "film_type": cinema_type,
        "film_genres": genres_list,
        "release_date": film.release_date.strftime("%Y"),
    }
    print(out_data)
    return out_data


def random_recommendation(session):
    max_id = session.query(Cinema).order_by(Cinema.id.desc()).first().id
    return get_film_info(session, randint(1, max_id))


def recommendation_for_user(session, user):
    pass