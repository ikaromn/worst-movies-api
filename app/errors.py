from http import HTTPStatus

from flask import Blueprint, jsonify

errors = Blueprint("errors", __name__)


@errors.app_errorhandler(HTTPStatus.NOT_FOUND)
def page_not_found(e):
    reponse = {
        "error": "Page Not Found",
        "status_code": HTTPStatus.NOT_FOUND,
    }

    return jsonify(reponse), HTTPStatus.NOT_FOUND


@errors.app_errorhandler(HTTPStatus.BAD_REQUEST)
def page_bad_request(e):
    reponse = {
        "error": "Bad Request Error",
        "status_code": HTTPStatus.BAD_REQUEST,
        "data": f"{e}",
    }

    return jsonify(reponse), HTTPStatus.BAD_REQUEST


@errors.app_errorhandler(HTTPStatus.METHOD_NOT_ALLOWED)
def page_method_not_allowed(e):
    reponse = {
        "error": "Method Not Allowed",
        "status_code": HTTPStatus.METHOD_NOT_ALLOWED,
        "data": f"Allowed methods: {e.valid_methods}",
    }

    return jsonify(reponse), HTTPStatus.METHOD_NOT_ALLOWED
