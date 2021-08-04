import operator
import time
import functools


def logger(function):
    def g(x, y):
        print("function: ", function.__name__)
        res = function(x, y)
        print(res)

    return g


def decorator(function):
    def inner(s):
        print("Someone called {}".format(function.__name__))
        print(function(s))

    return inner


# to_lower = decorator(to_lower)
@decorator
def to_lower(s):
    return s.lower()


to_lower("AAAAA")


def cancel(function):
    def inner(*args, **kwargs):
        print(function.__name__, "is canceled!")

    return inner


@cancel
def some_fun(x, y, name=None):
    print(name, "at {}:{}".format(x, y))


def timeit(function):
    def inner(*args, **kwargs):
        start = time.time()
        function(*args, **kwargs)
        end = time.time()
        print("Execution time of {} is {}".format(function.__name__, end - start))

    return inner


@timeit
def expensive_operation(*args, **kwargs):
    for i in range(1000):
        x = list(map(int, " 1 2 3 ".split() * i))


def counter(function):
    def inner(*args, **kwargs):
        inner.counter += 1
        print(function.__name__, "was executed {} times".format(inner.counter))

    inner.counter = 0
    return inner


@counter
def fun():
    pass


@counter
def fun1():
    pass


def safe_execution(function):
    def inner(*args, **kwargs):
        try:
            function(*args, **kwargs)
        except Exception as e:
            print("Exception has occurred with the arguments:", e)

    return inner


@safe_execution
def unsafe_func(a, b, c):
    raise RuntimeError(a, b, c)


class CalcCalls(object):
    def __init__(self, func):
        self.func = func
        functools.update_wrapper(self, func)
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.func(*args, **kwargs)
        self.counter += 1


# method = CalcCalls(method) -> __init__ && __call__ are required


@CalcCalls
def check(a):
    return a is None


class Calculate:
    def __init__(self, arg):
        self.arg = arg

    def __call__(self, function):
        functools.update_wrapper(self, function)

        def inner(*args, **kwargs):
            return self.arg * function(*args, **kwargs)

        return inner


@Calculate(2)  # method = Decorator(*args, **kwargs)(method)
def square(x):
    return x ** 2


def singleton(cls):
    """Make a class a Singleton class (only one instance)"""

    @functools.wraps(cls)
    def wrapper_singleton(*args, **kwargs):
        if not wrapper_singleton.instance:
            wrapper_singleton.instance = cls(*args, **kwargs)
        return wrapper_singleton.instance

    wrapper_singleton.instance = None
    return wrapper_singleton


@singleton
# TheOne = singleton(TheOne)
class TheOne:
    pass


if __name__ == "__main__":
    s = logger(operator.add)
    s(1, 2)

    s = logger(operator.mul)
    s(1, 2)

    some_fun(1, 2, "me")

    expensive_operation()

    fun()
    fun1()
    fun()
    fun1()
    fun()
    fun()
    fun1()

    unsafe_func(1, 2, 3)

    check(1)
    check(2)
    check(3)
    print(check.counter)

    print(TheOne)

    print(square(3))
