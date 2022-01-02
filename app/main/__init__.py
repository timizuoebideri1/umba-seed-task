from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(configuration):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(configuration)
    db.init_app(app)

    from app.users.models import Users
    from app.users.views import user_bp
    from app.users.api import UsersApi

    app.register_blueprint(user_bp)
    api.add_resource(UsersApi, '/api/users/profiles')

    return app
