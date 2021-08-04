from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

dir_name = os.path.abspath(os.path.dirname(__file__))
db_uri = "sqlite:///" + os.path.join(dir_name, "flasksql_1.db")

app.config.update(
    DEBUG=True,
    SECRET_KEY="something-secret",
    WTF_CSRF_ENABLED=False,
    SQLALCHEMY_DATABASE_URI=db_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db = SQLAlchemy(app)


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    job = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<Person {id}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "job": self.job,
        }


@app.route("/")
def index():
    people = Person.query.all()
    by_name = Person.query.filter_by(name="Semen").first()
    by_age = Person.query.filter(Person.age > 30).all()
    by_job = Person.query.filter(Person.job == "HR")

    sub = db.session.query(db.func.min(Person.age).label("min_age")).subquery()

    youngest = Person.query.join(sub, sub.c.min_age == Person.age).first()

    return jsonify(
        {
            "people": [p.to_dict() for p in people],
            "by_name": by_name.to_dict(),
            "by_age": [p.to_dict() for p in by_age],
            "by_job": [p.to_dict() for p in by_job],
        }
    )


if __name__ == "__main__":
    # creating tables in the database
    db.create_all()

    # delete all the records in Person
    Person.query.delete()

    # creating new ones
    ivan = Person(name="Ivan", age=3)
    sveta = Person(name="Sveta", age=32, job="HR")
    semen = Person(name="Semen", age=30, job="IT")
    kolya = Person(name="Kolya", age=23, job="HR")

    db.session.add(ivan)
    db.session.add(sveta)
    db.session.add(semen)
    db.session.add(kolya)

    db.session.commit()

    app.run()
