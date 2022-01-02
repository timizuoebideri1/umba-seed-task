from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(configuration):
    app = Flask(__name__)
    app.config.from_object(configuration)
    db.init_app(app)

    from app.users.models import Users
    from app.users.views import user_bp

    app.register_blueprint(user_bp)

    return app
