from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class MovieProducer(db.Model):
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    producer_id = db.Column(db.Integer, db.ForeignKey("producer.id"), primary_key=True)


class MovieStudio(db.Model):
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.id"), primary_key=True)
    studio_id = db.Column(db.Integer, db.ForeignKey("studio.id"), primary_key=True)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String, nullable=False)
    studios = db.relationship("Studio", secondary="movie_studio", backref="movies")
    producers = db.relationship("Producer", secondary="movie_producer", backref="movies")
    winner = db.Column(db.Boolean, default=False)


class Studio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


class Producer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
