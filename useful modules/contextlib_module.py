from contextlib import contextmanager
import contextlib
from contextlib import asynccontextmanager
import os
import io


class File(object):
    def __init__(self, filename, mode):
        print("__init__ in File")
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        print("__enter__ in File")
        self.file = open(file=self.filename, mode=self.mode)
        return self.file

    def __exit__(self, exception_type, exception_value, traceback):
        print("__exit__ in File")
        self.file.close()
        return exception_type is None


@contextmanager
def do_work(value):
    print("before yield, __enter__")
    yield value
    print("after yield, __exit__")


@contextmanager
def file(filename, mode):
    f = open(file=filename, mode=mode)
    yield f
    f.close()


def get_resource(*args, **kwargs):
    print("in get_resource")
    return object()


def release_resource(*args, **kwargs):
    print("in release_resource")


@contextmanager
def context_manager(*args, **kwargs):
    resource = get_resource(*args, **kwargs)
    try:
        yield resource
    finally:
        release_resource(*args, **kwargs)


def acquire_db_connection(*args, **kwargs):
    raise NotImplemented()


def release_db_connection(*args, **kwargs):
    raise NotImplemented()


@asynccontextmanager
async def get_connection():
    conn = await acquire_db_connection()
    try:
        yield conn
    finally:
        await release_db_connection(conn)


async def get_all_users():
    async with get_connection() as conn:
        return conn.query("SELECT ...")


"""
contextlib.closing(thing)
Return a context manager that closes thing upon completion of the block. This is basically equivalent to:
"""


@contextmanager
def my_closing(thing):
    try:
        yield thing
    finally:
        thing.close()


"""
contextlib.nullcontext(enter_result=None)
Return a context manager that returns enter_result from __enter__, 
but otherwise does nothing. It is intended to be used as a stand-in for an optional context manager, for example:
"""


def process_file(file_or_path):
    if isinstance(file_or_path, str):
        # If string, open file
        cm = open(file_or_path)
    else:
        # Caller is responsible for closing file
        cm = contextlib.nullcontext(file_or_path)

    with cm as file:
        file.close()
        # Perform processing on the file


def myfunction(arg, ignore_exceptions=False):
    if ignore_exceptions:
        # Use suppress to ignore all exceptions.
        cm = contextlib.suppress(Exception)
    else:
        # Do not ignore any exceptions, cm has no effect.
        cm = contextlib.nullcontext()
    with cm:
        pass  # Do something


class MyContext(contextlib.ContextDecorator):
    def __enter__(self):
        print(f"in the __enter__ of {self.__class__}")
        return self

    def __exit__(self, *args):
        print(f"in he __exit__ of {self.__class__}")
        return args[0] is None


def function():
    print("in the function")


def f():
    with MyContext():
        pass


"""
is equal to
"""


@MyContext()
def f():
    pass


"""
ContextDecorator can be used as mixin class
"""


class A:
    pass


class MyContext1(A, contextlib.ContextDecorator):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        return args[0] is None


"""
class contextlib.ExitStack
A context manager that is designed to make it easy to programmatically 
combine other context managers and cleanup functions, especially those that are
 optional or otherwise driven by input data.
 
enter_context(cm)

Enters a new context manager and adds its __exit__() method to the callback stack. 
The return value is the result of the context manager’s own __enter__() method.

push(exit)

Adds a context manager’s __exit__() method to the callback stack.
The passed in callback is returned from the function, allowing this method to be used as a function decorator.

callback(callback, *args, **kwds)

Accepts an arbitrary callback function and arguments and adds it to the callback stack.
Unlike the other methods, callbacks added this way cannot suppress exceptions 
(as they are never passed the exception details).
The passed in callback is returned from the function, allowing this method to be used as a function decorator.

pop_all()

Transfers the callback stack to a fresh ExitStack instance and returns it. No callbacks are invoked by this operation 
- instead, they will now be invoked when the new stack is closed 
(either explicitly or implicitly at the end of a with statement).

close()

Immediately unwinds the callback stack, invoking callbacks in the reverse order of registration.
For any context managers and exit callbacks registered, the arguments passed in will indicate 
that no exception occurred.

"""

with contextlib.ExitStack() as stack:
    files = [stack.enter_context(open(filename)) for filename in ["to_open.txt"]]
    # All opened files will automatically be closed at the end of
    # the with statement, even if attempts to open files later
    # in the list raise an exception

    close_files = stack.pop_all().close
    # If opening any file fails, all previously opened files will be
    # closed automatically. If all files are opened successfully,
    # they will remain open even after the with statement ends.
    # close_files() can then be invoked explicitly to close them all.
    close_files()


if __name__ == "__main__":
    with File("to_open.txt", mode="w") as f:
        f.write("some data\n")

    with do_work(14) as w:
        print(w)

    with file("to_open.txt", "r") as f:
        print(f.read())

    with context_manager() as obj:
        # Resource is released at the end of this block,
        # even if code in the block raises an exception
        print(obj)
        print(dir(obj))
        # raise ValueError()

    with my_closing(open("to_open.txt")) as file:
        print(file.read())

    with contextlib.closing(open("to_open.txt")) as file:
        print(file.read())

    with contextlib.suppress(FileNotFoundError):
        os.remove("temp.txt")

    f = io.StringIO()
    with contextlib.redirect_stdout(f):
        print("something in redirected stdout")

    print(f.getvalue())

    with contextlib.redirect_stderr(f):
        pass

    """
     ContextDecorator
    """

    with MyContext() as e:
        function()
