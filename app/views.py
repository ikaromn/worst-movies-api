from flask import Blueprint


main_blueprint = Blueprint("main", __name__)


@main_blueprint.route("/", methods=["GET"])
def home():
    return {"Hello": "World"}
