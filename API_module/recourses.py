from flask_restful import Resource
from flask import jsonify, request

from data import db_session
from data.user import User
from data.user_nets import UserNet

from API_module.recomend_module import random_recommendation

SUCCESS_ERROR = "success"
class UserHandler(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        print("post", json_data)

        session = db_session.create_session()

        if not (session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                        UserNet.net_ident == json_data["net_ident"]).first() is None):
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
                                                 UserNet.net_ident == json_data["net_ident"]).first()
        if user_net is None:
            return jsonify({"error": "User net not found"})

        user = session.query(UserNet).filter(User.id == user_net.user_id).first()

        if json_data["command"] == "put film":
            pass
        elif json_data["command"] == "change age":
            pass
        session.commit()
        return jsonify({"user_state": False})

    def get(self):
        json_data = request.get_json(force=True)
        print("get", json_data)

        session = db_session.create_session()

        user_net = session.query(UserNet).filter(UserNet.net_name == json_data["net"],
                                                 UserNet.net_ident == json_data["net_ident"]).first()

        if user_net is None:
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "film_info": random_recommendation(session),
                "error": "User net not found",
            })

        if json_data["command"] == "random film":
            return jsonify({
                "net": json_data["net"],
                "net_id": json_data["net_id"],
                "film_info": random_recommendation(session),
                "error": SUCCESS_ERROR,
            })

        if json_data["command"] == "personal recommend":
            return jsonify({
                    "net": json_data["net"],
                    "net_id": json_data["net_id"],
                    "film_info": random_recommendation(session),
                    "error": SUCCESS_ERROR,
                })