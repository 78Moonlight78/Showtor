from flask_restful import Resource
from flask import jsonify, request

from data import db_session
from data.user import User
from data.user_nets import UserNet
from data.ratings import Rating
from data.cinema import Cinema

from API_module.recomend_module import random_recommendation, personal_recommendation

from json import loads, dumps


SUCCESS_ERROR = "success"


class UserHandler(Resource):
    def post(self):
        # добавление нового пользователя
        json_data = request.get_json(force=True)
        print("post", json_data)

        session = db_session.create_session()

        # проверка: есть ли пользователь
        if not (session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                              UserNet.net_ident == json_data["net_id"]).first() is None):
            print("User is generated")
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "error": "User is generated",
            })

        user = User()
        session.add(user)
        user_id = session.query(User).order_by(User.id.desc()).first().id

        print(user_id)
        net = UserNet(
            user_id=user_id,
            net_name=json_data["net"],
            net_ident=json_data["net_id"],
        )
        session.add(net)
        session.commit()
        return jsonify({
            "net": json_data["net"],
            "net_id": json_data["net_id"],
            "error": SUCCESS_ERROR,
        })
    # -------------------------------------post-------------------------------------

    def put(self):
        json_data = request.get_json(force=True)
        print("put", json_data)

        session = db_session.create_session()

        user_net = session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                                 UserNet.net_ident == json_data["net_id"]).first()

        # проверка: зарегистрирована ли сеть пользователя
        if user_net is None:
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "error": "User net not found"})

        user = session.query(User).filter(User.id == user_net.user_id).first()

        # добавить фильм в просмотренные или понравившиеся, непонравишиеся
        if json_data["command"] == "put film":
            error_cinemas = list()
            for cinema_name in json_data["argument"]["cinemas"]:
                cinema = session.query(Cinema).filter(Cinema.name == cinema_name, Cinema.is_visible == True).first()
                if cinema is None:
                    cinema = Cinema(name=cinema_name)
                    session.add(cinema)
                    session.commit()
                    error_cinemas.append(cinema_name)
                    cinema = session.query(Cinema).filter(Cinema.name == cinema_name, Cinema.is_visible == True).first()
                    print(cinema.name)


                rating = Rating(
                        user_id=user.id,
                        cinema_id=cinema.id,
                        rating=10 if json_data["argument"]["estimation"] == "like" else
                                        1 if json_data["argument"]["estimation"] == "not like" else 0,
                        is_rating=False
                    )
                session.add(rating)
            session.commit()
            return jsonify({"net": json_data["net"],
                            "net_id": json_data["net_id"],
                            "error": SUCCESS_ERROR if not bool(error_cinemas) else "not found cinemas",
                            "error cinemas": error_cinemas})

        # добавить фильм в планируемые
        if json_data["command"] == "put film to stack":
            if session.query(Cinema).filter(Cinema.name == json_data["argument"],
                                            Cinema.is_visible == True).first() is None:
                return jsonify({"net": json_data["net"],
                                "net_id": json_data["net_id"],
                                "error": "not found cinema"})

            user_plan = loads(user.user_plan)
            user_plan.append(json_data["argument"])
            user.user_plan = dumps(user_plan)
            session.commit()
            return jsonify({"net": json_data["net"],
                            "net_id": json_data["net_id"],
                            "error": SUCCESS_ERROR})

        session.commit()
        return jsonify({
            "net": json_data["net"],
            "net_id": json_data["net_id"]})
        #  ---------------------------------------put--------------------------------------------------

    def get(self):
        json_data = request.get_json(force=True)
        print("get", json_data)

        session = db_session.create_session()

        user_net = session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                                 UserNet.net_ident == json_data["net_id"]).first()

        # если сеть пользователя не найдена
        if user_net is None:
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "film_info": random_recommendation(session),
                "error": "User net not found",
            })

        user = session.query(User).filter(User.id == user_net.user_id).first()  # пользователь, который написал комманду
        if user is None:
            print("ghfhghfhhghrfhhrehr")

        print(user.id)

        # случайный фильм
        if json_data["command"] == "random film":
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "film_info": random_recommendation(session),
                "error": SUCCESS_ERROR,
            })

        # персональная рекомендация
        if json_data["command"] == "personal recommend":
            try:
                return jsonify({
                        "net": json_data["net"],
                        "net_id": json_data["net_id"],
                        "film_info": personal_recommendation(session, json_data["argument"]),
                        "error": SUCCESS_ERROR,
                    })
            except KeyError:
                return jsonify({
                    "net": json_data["net"],
                    "net_id": json_data["net_id"],
                    "error": "bad argument",
                })

        # получить список фильмов, которые пользователь планирует посмотерть
        if json_data["command"] == "get all stack list":
            return jsonify({
                "plan": loads(user.user_plan),
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "error": SUCCESS_ERROR})

        # получение всех просмотренных фильмов
        if json_data["command"] == "all watched":
            watched_cinemas = session.query(Rating).filter(Rating.user_id == user.id, Rating.is_visible == True).all()
            out_cinemas = list()
            for cinema in watched_cinemas:
                this_cinema = session.query(Cinema).filter(Cinema.id == cinema.cinema_id,
                                                           Cinema.is_visible == True).first()
                if not(this_cinema is None):
                    out_cinemas.append(this_cinema.name)

            return jsonify({
                    "watched cinemas": out_cinemas,
                    "net": json_data["net"],
                    "net_id": json_data["net_id"],
                    "error": SUCCESS_ERROR,
                })
        #  ------------------------------------get--------------------------------------------

