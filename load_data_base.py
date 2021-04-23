from data import db_session
from data.cinema import Cinema
from data.cinema_type import CinemaType
from data.genre import Genre
from datetime import date
import csv

import json


db_session.global_init("db/showtor_db.db")
#session = db_session.create_session()


def get_date_from_string(string):
    print(string)
    out_date = ''
    date_found = False
    try:
        for i in range(len(string)):
            if date_found and string[i] == ")":
                return out_date

            if date_found:
                out_date += string[i]

            if string[i] == "(" and string[i+1].isdigit():
                date_found = True
    except Exception:
        print("err")

    return out_date


def genre_in_base(genre):
    session = db_session.create_session()
    for i in session.query(Genre).all():
        if i.name == genre:
            return i.id
    return -1


out_line_num = 0

with open("C:\\Users\\Пользователь\\Downloads\\ml-25m\\movies.csv", encoding="utf8") as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    session = db_session.create_session()
    for line in reader:
        if out_line_num != 0:
            print(out_line_num)
            tags = line[2].split("|")
            relise_date = get_date_from_string(line[1])

            cinema_type = 1
            if "Animation" in tags:
                tags.remove("Animation")
                cinema_type = 2

            for i in range(len(tags)):
                if genre_in_base(tags[i]) == -1:
                    genre = Genre(
                        name=tags[i]
                    )
                    session.add(genre)
                    tags[i] = session.query(Genre).order_by(Genre.id.desc()).first().id
                    session.commit()
                else:
                    tags[i] = session.query(Genre).filter(Genre.name == tags[i]).first().id

            tags_json = json.dumps(tags)

            cinema = Cinema(
                type=cinema_type,
                genres=tags_json,
                name=line[1],
                release_date=date(year=int(relise_date), month=1, day=1)
            )
            session.add(cinema)

        out_line_num += 1
        if out_line_num % 100 == 0:
            session.commit()
    session.commit()