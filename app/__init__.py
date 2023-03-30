from flask import Flask

from .views import api
from .init_data import init_db
from .models import db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    init_db(app)

    return app
