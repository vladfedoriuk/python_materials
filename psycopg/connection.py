class DbNotSpecifiedError(Exception):
    pass


class Cursor(object):
    def __init__(self, **kwargs):

        if "database" not in kwargs:
            raise DbNotSpecifiedError("database attribute wasn't found")

        if "module" not in kwargs:
            raise DbNotSpecifiedError("Module with database API wasn't found")

        self.db = kwargs.get("module")
        self.connection_args = kwargs.copy()
        self.connection_args.pop("module")

    def __enter__(self):

        try:
            self.connection = self.db.connect(**self.connection_args)
            self.cursor = self.connection.cursor()
        except self.db.Error as db_err:
            print(f"Error: {db_err}")
            raise db_err
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        If __exit__ returns True, the exception is suppressed.
        """
        self.cursor.close()
        if self.connection:
            self.connection.commit()
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
                return return_value

        return inner
