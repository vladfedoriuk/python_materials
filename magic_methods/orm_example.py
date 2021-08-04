"""
ORM example

The following code is simplified skeleton showing how data descriptors
could be used to implement an object relational mapping.

The essential idea is that the data is stored in an external database. 
The Python instances only hold keys to the database’s tables. 
Descriptors take care of lookups or updates:
"""

from contextlib import contextmanager, closing
import sqlite3 as db

DB_NAME = "orm.db"


@contextmanager
def connect_to(db_name):
    try:
        connection = db.connect(db_name)
        yield connection
        connection.commit()
    except db.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            connection.close()


class Field(object):
    def __set_name__(self, owner, name):  # owner = Movie, owner.key = 'title'
        self.fetch = f"Select {name} FROM {owner.__tablename__} WHERE {owner.key} = ?;"
        self.store = (
            f"UPDATE {owner.__tablename__} SET {name} = ? WHERE {owner.key} = ?;"
        )

    def __get__(self, obj, obtype=None):
        with connect_to(DB_NAME) as connection:
            with closing(connection.cursor()) as cursor:
                return cursor.execute(self.fetch, [obj.key]).fetchone()[0]

    def __set__(self, obj, value):
        with connect_to(DB_NAME) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(self.store, [value, obj.key])


class Movie(object):
    __tablename__ = "Movies"
    key = "title"
    director = Field()
    year = Field()

    def __init__(self, key):
        self.key = key


if __name__ == "__main__":
    movie = Movie("b")
    movie.year = 1985
    movie.director = "Robert Zemekis"
    print(movie.year)
