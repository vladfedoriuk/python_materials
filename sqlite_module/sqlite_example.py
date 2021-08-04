import sqlite3 as db
from contextlib import closing, contextmanager
import datetime


class DbNotSpecifiedError(Exception):
    pass


class Connection(object):
    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)

    def __enter__(self):
        if "database" not in self.__dict__:
            raise DbNotSpecifiedError("database attribute wasn't found")
        try:
            self.connection = db.connect(**self.__dict__)
            self.cursor = self.connection.cursor()
        except db.Error as db_err:
            print(f"Error: {db_err}")
            raise db_err
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If __exit__ returns True, the exception is suppressed.
        """
        self.cursor.close()
        if self.connection:
            self.connection.close()
        if exc_type:
            print(f"Exception type: {exc_type}")
            print(f"Value: {exc_val}")
            print(f"Traceback: {exc_tb}")
        else:
            return True

    def __call__(self, function):
        def inner(*args, **kwargs):
            with self as cursor:
                inner.__setattr__("cursor", cursor)
                inner.__setattr__("connection", self.connection)
                return_value = function(*args, **kwargs)
                self.connection.commit()
                return return_value

        return inner


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


def create_db(db_name):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT sqlite_version();")
            record = cursor.fetchall()
            print("Database version information: ", record)


def create_table(db_name):
    try:
        connection = db.connect(db_name)
        with closing(connection.cursor()) as cursor:
            #  cursor.execute(
            #      'DROP TABLE person;'
            #  )
            create_query = """  CREATE TABLE person (
                                id INTEGER PRIMARY KEY NOT NULL,
                                name TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                joining_date DATETIME,
                                salary REAL NOT NULL);
                           """
            cursor.execute(create_query)
            cursor.execute('SELECT sql FROM sqlite_master WHERE name="person";')
            data = cursor.fetchall()
            print(data)
            connection.commit()
    except db.Error as er:
        print(f"Error {er}")
    finally:
        # print(locals()) There is a sqlite3.Connection object
        if connection:
            connection.close()


def insert_value(db_name, *values):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("INSERT INTO person VALUES (?, ?, ?, ?, ?);", tuple(values))
            connection.commit()


def insert_many(db_name, values):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.executemany(
                "INSERT INTO person VALUES (?, ?, ?, ?, ?);", iter(values)
            )
            print(f"{cursor.rowcount} values were successfully inserted into the table")
            connection.commit()


def select(db_name):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("SELECT * FROM person;")
            data = cursor.fetchall()
            print(".fetchall results")
            for row in data:
                print("".ljust(5, "-"))
                print("id = ", row[0])
                print("name = ", row[1])
                print("email = ", row[2])
                print("join date = ", row[3])
                print("salary = ", row[4])
            print(data)

            cursor.execute("SELECT * FROM person;")
            print("First result")
            print(cursor.fetchone())  # select only 1 record ( the first one )

            cursor.execute("SELECT * FROM person;")
            print("First two result")
            print(cursor.fetchmany(2))  # select only 2 records ( the first two )


def update(db_name, id):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(
                "UPDATE person SET salary = 1000, email = 'j@gmail.com' WHERE id = ?",
                (id,),
            )


def update_many(db_name, records):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.executemany(
                "UPDATE person SET salary=? WHERE id = ? ", iter(records)
            )
            print(cursor.rowcount)


def delete(db_name, id):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute("DELETE FROM person WHERE id = ?", (id,))


def delete_many(db_name, records):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.executemany("DELETE FROM person WHERE id=?", records)


def commands_from_file(db_name, filename):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            with open(filename) as file:
                sql = file.read()
            cursor.executescript(sql)  # equivalent to '.read filename'
            cursor.execute('SELECT * from sqlite_master WHERE type="table"')
            print(cursor.fetchall())


def using_blob(db_name, filename):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            with open(filename, "rb") as file:
                blob_data = file.read()
            cursor.execute(
                """CREATE TABLE files(
                                name TEXT UNIQUE NOT NULL,
                                data BLOB NOT NULL
                                );
                       """
            )
            cursor.execute(
                "INSERT INTO files VALUES(?, ?)",
                (
                    filename,
                    blob_data,
                ),
            )
            cursor.execute("SELECT * FROM files")
            print(cursor.fetchall())


def my_func(string):
    return str(string).title()


def custom_function(db_name):
    with connect_to(db_name) as connection:
        with closing(connection.cursor()) as cursor:
            connection.create_function("CAPITALIZE", 1, my_func)
            cursor.execute("SELECT CAPITALIZE(name) FROM person;")
            print(cursor.fetchone())
            cursor.execute("SELECT * FROM person;")
            print(cursor.fetchall())


@Connection(database="test.db", timeout=20)
def my_experiment_with_context_decorator():
    cursor = my_experiment_with_context_decorator.cursor
    cursor.execute("SELECT * FROM person;")
    data = cursor.fetchall()
    print(data)


@Connection(database="test.db", detect_types=db.PARSE_DECLTYPES | db.PARSE_COLNAMES)
def datetime_example(*values):
    cursor = datetime_example.cursor
    """ cursor.execute('''
                        CREATE TABLE new_developers (
                            id INTEGER PRIMARY KEY NOT NULL,
                            name TEXT NOT NULL,
                            joining_date timestamp
                        );        
                   ''') """
    # cursor.execute('INSERT INTO new_developers VALUES (?, ?, ?)', tuple(values))
    cursor.execute("SELECT * FROM new_developers;")
    data = cursor.fetchone()
    print(f"Data: {data}")
    print(f"Type of joining_date: {type(data[2])}")
    print("Total changes: ", datetime_example.connection.total_changes)


@Connection(database="test.db")
def backup_example():
    connection = backup_example.connection
    with Connection(database="backup.db") as cursor:
        b_connection = cursor.connection
        connection.backup(
            b_connection,
            progress=lambda status, remaining, total: print(
                f"Copied {total - remaining} of {total}"
            ),
        )


"""
Python type	 SQLite type
None	        NULL
int	            INTEGER
float	        REAL
str	            TEXT
bytes	        BLOB
"""

if __name__ == "__main__":
    # create_db('test.db')
    # create_table('test.db')
    # insert_value('test.db', 1, 'Vlad', 'v@g.com', '20-12-2020', 0.0)
    # select('test.db')
    records_to_insert = [
        (2, "Jos", "jos@gmail.com", "2019-01-14", 9500),
        (3, "Chris", "chris@gmail.com", "2019-05-15", 7600),
        (4, "Jonny", "jonny@gmail.com", "2019-03-27", 8400),
    ]
    # insert_many('test.db', records_to_insert)
    # update('test.db', 2)
    # select('test.db')
    records_to_update = [(9701, 4), (7800, 3), (8400, 2)]
    # update_many('test.db', records_to_update)
    # select('test.db')
    # delete('test.db', 4)
    # select('test.db',)
    # records_to_delete = [(2, ), (3, )]
    # delete_many('test.db', records_to_delete)
    # select('test.db')
    # commands_from_file('test.db', 'commands.sql')
    # using_blob('test.db', 'commands.sql')
    # insert_many('test.db', records_to_insert)
    # custom_function('test.db')
    # cls = type('Try', (object, ), {'attempt': 'accomplished'})
    # t = cls()
    # print(t.attempt)
    # print(t)
    # print(cls)
    # t.attempt = 'something else'
    # print(cls.attempt)
    # k = cls()
    # print(k.attempt, t.attempt, cls.attempt)
    # my_experiment_with_context_decorator()
    """try:
        with db.connect('test.db') as connection:
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM person;')
            print(cursor.fetchall())
            cursor.close()
        connection.close()
    except db.Error as err:
        print(f'Error: {err}')"""
    # datetime_example(1, 'me', datetime.datetime.now())
    backup_example()
