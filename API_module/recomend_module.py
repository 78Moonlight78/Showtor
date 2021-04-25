from data import db_session
from data.user import User
from data.user_nets import UserNet
from data.cinema import Cinema
from data.cinema_type import CinemaType
from data.genre import Genre

from random import randint

from json import loads

from sqlalchemy import or_


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
        "film": "film found"
    }
    print(out_data)
    return out_data


def random_recommendation(session):
    max_id = session.query(Cinema).order_by(Cinema.id.desc()).first().id
    return get_film_info(session, randint(1, max_id))


def personal_recommendation(session, argument):
    cinema_type = session.query(CinemaType).filter(CinemaType.name == argument["cinema_type"]).first()
    if cinema_type is None:
        return {"film": "film not found",
                "cinema_type": "cinema type not found"}

    cinema_genre = session.query(Genre).filter(Genre.name == argument["genre"]).first()
    if cinema_genre is None:
        if cinema_genre is None:
            return {"film": "film not found",
                    "genre": "genre not found"}

    # film = None
    if cinema_type.id in [i.id for i in session.query(CinemaType).filter(
            CinemaType.name.in_(["аниме", "сериал", "мультсериал"])).all()]:
        film = session.query(Cinema).filter(Cinema.type == cinema_type.id,
                                            Cinema.is_visible == True,
                                            Cinema.number_of_episodes <= int(argument["number of episodes"]),
                                            or_(Cinema.genres.like(f"%{str(cinema_genre.id)},%"),
                                                Cinema.genres.like(f"%{str(cinema_genre.id)}]%")))

    if cinema_type.id in [i.id for i in session.query(CinemaType).filter(
            CinemaType.name.in_(["фильм", "мультфильм"])).all()]:
        film = session.query(Cinema).filter(Cinema.type == cinema_type.id,
                                            Cinema.is_visible == True,
                                            or_(int(argument["min duration"]) <= Cinema.duration,
                                                Cinema.duration <= int(argument["max duration"]),
                                                Cinema.duration == None),
                                            or_(Cinema.genres.like(f"%{str(cinema_genre.id)},%"),
                                                Cinema.genres.like(f"%{str(cinema_genre.id)}]%")))

    if argument["release date"] == "not specified":
        films = film.all()
        if films is None:
            return {"film": "film not found",
                    "cinema_type": "cinema type found"}
        out_film = films[randint(0, len(films))-1]

    elif argument["release date"] == "new":
        films = film.all()
        out_film = film.first()

        if out_film is None:
            return {"film": "film not found",
                    "cinema_type": "cinema type found"}

        for this_film in films:
            if out_film.release_date < this_film.release_date:
                out_film = this_film

    elif argument["release date"] == "old":
        films = film.all()
        out_film = film.first()

        if out_film is None:
            return {"film": "film not found",
                    "cinema_type": "cinema type found"}

        for this_film in films:
            if out_film.release_date > this_film.release_date:
                out_film = this_film

    return get_film_info(session, out_film.id)
