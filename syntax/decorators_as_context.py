import contextlib
from functools import wraps

class Tag(contextlib.ContextDecorator):
    def __init__(self, tag):
        self.tag = tag

    def __enter__(self):
        print("<{}>".format(self.tag))
        return self

    def __exit__(self, *args):
        print("</{}>".format(self.tag))
        return args[0] is None


@Tag("p")
def non_html():
    print("paragraph")


non_html()
