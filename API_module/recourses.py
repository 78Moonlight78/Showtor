from flask_restful import Resource
from flask import jsonify, request

from data import db_session
from data.user import User
from data.user_nets import UserNet
from data.ratings import Rating
from data.cinema import Cinema

from API_module.recomend_module import random_recommendation, personal_recommendation


SUCCESS_ERROR = "success"


class UserHandler(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print("post", json_data)

        session = db_session.create_session()

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
        # print(user_id)

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

    def put(self):
        json_data = request.get_json(force=True)
        print("put", json_data)

        session = db_session.create_session()

        user_net = session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                                 UserNet.net_ident == json_data["net_id"]).first()
        if user_net is None:
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "error": "User net not found"})

        user = session.query(UserNet).filter(User.id == user_net.user_id).first()

        if json_data["command"] == "put film":
            error_cinemas = list()
            for cinema_name in json_data["argument"]["cinemas"]:
                cinema = session.query(Cinema).filter(Cinema.name == cinema_name, Cinema.is_visible == True).first()
                if cinema is None:
                    error_cinemas.append(cinema_name)
                else:
                    rating = Rating(
                        user_id=user.id,
                        cinema_id=cinema.id,
                        rating=10 if json_data["argument"]["estimation"] == "like" else 1,
                        is_rating=False
                    )
                    session.add(rating)
            session.commit()
            return jsonify({"net": json_data["net"],
                            "net_id": json_data["net_id"],
                            "error": SUCCESS_ERROR if not bool(error_cinemas) else "not found cinemas",
                            "error cinemas": error_cinemas})

        elif json_data["command"] == "change age":
            pass
        elif json_data["command"] == "put film to stec":
            pass

        session.commit()
        return jsonify({
            "net": json_data["net"],
            "net_id": json_data["net_id"],
            "user_state": False})

    def get(self):
        json_data = request.get_json(force=True)
        print("get", json_data)

        session = db_session.create_session()

        user_net = session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                                 UserNet.net_ident == json_data["net_id"]).first()

        if user_net is None:
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "film_info": random_recommendation(session),
                "error": "User net not found",
            })

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

        if json_data["command"] == "get last stec fim":
            pass

        if json_data["command"] == "get all stec list":
            pass

        if json_data["command"] == "recommend":
            pass