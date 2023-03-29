from flask import Flask

from .views import main_blueprint
from .models import db


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    return app
