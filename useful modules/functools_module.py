import functools
from singledispatchmethod import singledispatchmethod


def timeit(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        import datetime

        start = datetime.datetime.now()
        res = function(*args, **kwargs)
        end = datetime.datetime.now()
        print("Elapsed time: {} [secs]".format(end - start))
        return res

    return inner


@functools.lru_cache(maxsize=126)
@timeit
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@functools.total_ordering
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age


"""
functools.partial(func, *args, **keywords)¶
Return a new partial object which when called will behave like func called with the positional arguments args and 
keyword arguments keywords.
If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, 
they extend and override keywords.
"""


def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)

    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc


class Cell(object):
    def __init__(self):
        self.__alive = True

    def set_state(self, state):
        self.__alive = bool(state)

    @property
    def alive(self):
        return self.__alive

    set_alive = functools.partialmethod(set_state, True)
    set_dead = functools.partialmethod(set_state, False)


@functools.singledispatch
def print_obj(obj):
    print("Object: ", obj)


@print_obj.register(int)
def print_int(i):
    print("Int: ", i)


@print_obj.register(list)
def print_list(l):
    print("List: ", l)


@functools.singledispatch
def represent(object):
    print("object is", object)


@represent.register
def _(arg: list) -> list:
    print("list is")
    for i, el in enumerate(arg):
        print(i, el, end=" ")
    print()
    return arg * 2


@represent.register
def _(arg: int) -> int:
    print("int is", arg)
    return arg + 2


class Parser:
    def __init__(self, **kwargs):
        for k, w in kwargs:
            super(Parser, self).__setattr__(k, w)
        self.print_arg = functools.singledispatch(self._print_arg)
        self.print_int = self.print_arg.register(int, self._print_int)
        self.print_list = self.print_arg.register(list, self._print_list)

    def _print_arg(self, arg):
        print("Got object: ", arg)

    def _print_int(self, arg):
        print("Got int: ", arg)

    def _print_list(self, arg):
        print("Got list: ", arg)


class Negator(object):
    @singledispatchmethod
    def negate(self, arg):
        raise NotImplementedError("cannot negate this argument")

    @negate.register
    def _(self, arg: int):
        return -arg

    @negate.register
    def _(self, arg: bool):
        return not arg


if __name__ == "__main__":
    print([fibonacci(x) for x in range(100)])
    print()
    fibonacci(110)
    print(fibonacci.cache_info())

    p = Person("Vlad", 19)
    p2 = Person("Dasha", 20)
    p3 = Person("Katia", 18)

    print(p2 > p)
    print(p3 <= p)

    basetwo = functools.partial(int, base=2)
    basetwo.__doc__ = "Converting a binary string to integer"
    print(basetwo("110110"))
    print(basetwo.func)
    print(basetwo.args)
    print(basetwo.keywords)

    c = Cell()
    c.set_dead()
    print(c.alive)

    print_obj("a")
    print_obj(2)
    print_obj([1, 2, 3])
    print(print_obj.dispatch(list))
    print(print_obj.registry.keys())

    represent(map)
    represent(2)
    represent([1, 2, 3])
    print(represent.dispatch(int))
    print(represent.registry.keys())
    print(represent.dispatch(list).__annotations__)

    p = Parser()
    p.print_arg(1)
    p.print_arg([1, 2, 3])
    p.print_arg("some")
    print(p.print_arg.dispatch(int))
    print(p.print_arg.registry.keys())

    negator = Negator()
    print(negator.negate(1))
    print(not 2)
    print(negator.negate(False))
    try:
        print(negator.negate(dict))
    except NotImplementedError as e:
        print(e)
