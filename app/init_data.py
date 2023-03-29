import csv

from .models import db, Movie, Producer, Studio


def init_db(app):
    with app.app_context():
        db.create_all()
        with open("data.csv", mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                winner = row["winner"].lower() == "yes"
                movie = Movie(
                    year=int(row["year"]),
                    title=row["title"],
                    winner=winner,
                )

                db.session.add(movie)

                producers = row["producers"].replace(", and", ";")
                producers = producers.replace(",", ";")
                producers = producers.replace(" and ", ";")

                for producer_name in producers.split(";"):
                    producer_name = producer_name.strip()
                    producer = Producer.query.filter_by(name=producer_name).first()
                    if not producer:
                        producer = Producer(name=producer_name)
                        db.session.add(producer)
                    movie.producers.append(producer)
                
                for studio_name in row["studios"].split(","):
                    studio_name = studio_name.strip()
                    studio = Studio.query.filter_by(name=studio_name).first()
                    if not studio:
                        studio = Studio(name=studio_name)
                        db.session.add(studio)
                    movie.studios.append(studio)

        db.session.commit()
