from flask import Flask
from flask_restful import Api

from API_module.recourses import UserHandler

from data import db_session

app = Flask(__name__)
api = Api(app)

api.add_resource(UserHandler, '/api/testing')
db_session.global_init("db/showtor_db.db")
app.run()