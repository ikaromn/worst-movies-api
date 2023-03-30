from flask import Blueprint, jsonify
from sqlalchemy import func

from app.errors import errors
from app.models import Movie, MovieProducer, Producer, db
from app.utils import get_producer_win_intervals

api = Blueprint("main", __name__)
api.register_blueprint(errors)


@api.route("/", methods=["GET"])
def home():
    return {"Hello": "World"}


@api.route("/prize-ranges/", methods=["GET"])
def prize_ranges():
    # Subquery to get producers that received more than 1 prize
    prizes_count_subquery = (
        db.session.query(
            MovieProducer.producer_id,
        )
        .join(Movie, Movie.id == MovieProducer.movie_id)
        .filter(Movie.winner == True)
        .group_by(MovieProducer.producer_id)
        .having(func.count(MovieProducer.movie_id) >= 2)
        .subquery()
    )

    # Get the name of producer and the year that him received the prizes
    winning_producers = (
        db.session.query(
            Producer.name.label("name"),
            Movie.year.label("year"),
        )
        .join(MovieProducer, MovieProducer.producer_id == Producer.id)
        .join(Movie, Movie.id == MovieProducer.movie_id)
        .join(prizes_count_subquery, prizes_count_subquery.c.producer_id == Producer.id)
        .filter(Movie.winner == True)
        .order_by(Producer.name, Movie.year)
        .all()
    )
    return jsonify(get_producer_win_intervals(winning_producers))
