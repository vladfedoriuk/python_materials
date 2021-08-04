import functools


def decorator(cls):
    class Decorator(object):
        def __init__(self, value):
            functools.update_wrapper(self, cls)
            if isinstance(value, cls):
                self.obj = value
            elif isinstance(value, Decorator):
                self.obj = value.obj
            else:
                self.obj = cls(value)

        def __add__(self, other):
            print(
                "Addition operation\n{} + {} = {}".format(
                    self, other, self.obj + other.obj
                )
            )
            return Decorator(self.obj + other.obj)

        def __mul__(self, other):
            print(
                "Multiplication operation\n{} * {} = {}".format(
                    self, other, self.obj * other.obj
                )
            )
            return Decorator(self.obj * other.obj)

        def __truediv__(self, other):
            print(
                "Division operation\n{} / {} = {}".format(
                    self, other, self.obj / other.obj
                )
            )
            return Decorator(self.obj / other.obj)

        def __str__(self):
            return "({} containing {})".format(cls.__name__, self.obj.value)

        def __call__(self):
            raise NotImplemented()

    return Decorator


@decorator
class MathObject:
    """Class representing math objects"""

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return MathObject(self.value + other.value)

    def __mul__(self, other):
        return MathObject(self.value * other.value)

    def __truediv__(self, other):
        return MathObject(self.value / other.value)

    def __call__(self):
        raise NotImplemented()


def timeit(function):
    def inner(*args, **kwargs):
        import datetime

        start = datetime.datetime.now()
        res = function(*args, **kwargs)
        end = datetime.datetime.now()
        print("Elapsed time is {} [secs]".format(end - start))
        return res

    return inner


def time_all(cls):
    class TimeAll(object):
        def __init__(self, *args, **kwargs):
            self.obj = cls(*args, **kwargs)

        def __getattribute__(self, item):
            try:
                x = super(TimeAll, self).__getattribute__(item)
            except AttributeError:
                pass
            else:
                return x
            x = self.obj.__getattribute__(item)
            if isinstance(x, type(self.obj.__init__)):
                return timeit(x)
            else:
                return x

    return TimeAll


@time_all
class SomeClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self, val):
        import time

        time.sleep(3)
        return (self.a + self.b) * val


# class decorating class
class TimeAll2(object):
    def __init__(self, cls):
        self.cls = cls

    def __call__(
        self, *args, **kwargs
    ):  # __call__ will play role of  __new__ + __init__
        self.obj = self.cls(*args, **kwargs)
        return self

    def __getattribute__(self, item):
        try:
            x = super(TimeAll2, self).__getattribute__(item)
        except AttributeError:
            pass
        else:
            return x

        x = self.obj.__getattribute__(item)
        if isinstance(x, type(self.__init__)):
            return timeit(x)
        return x


@TimeAll2
class SomeClass2(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self, val):
        import time

        time.sleep(3)
        return (self.a + self.b) * val


class TimeAll3(object):
    def __init__(self, *args, **kwargs):
        super(TimeAll3, self).__init__()
        self.__cls = None
        for k, v in kwargs.items():
            self.k = v

    def __call__(self, *args, **kwargs):
        if not kwargs and len(args) == 1 and isinstance(args[0], type(type(self))):
            if self.__cls is None:
                self.__cls = args[0]
        else:
            if self.__cls:
                self.__obj = self.__cls(*args, **kwargs)
        return self

    def __getattribute__(self, item):
        try:
            x = super(TimeAll3, self).__getattribute__(item)
        except AttributeError:
            pass
        else:
            return x

        x = self.__obj.__getattribute__(item)
        if isinstance(x, type(self.__init__)):
            print(self.__dict__)
            return timeit(x)
        return x


@TimeAll3(x=3, y=4)
class SomeClass3(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calc(self, val):
        import time

        time.sleep(3)
        return (self.a + self.b) * val


a = MathObject(2)
b = MathObject(3)
c = a + b
print(c)
c = c * a
print(c)
print(MathObject.__module__)
print(MathObject.__name__)
print(MathObject.__doc__)

print(c.__doc__)
print(c.__module__)
print(c.__name__)

s = SomeClass(1, 2)
print(s.a)
print(s.b)
print(s.calc(3))

print("SomeClass 2")
s = SomeClass2(1, 2)
print(s.a)
print(s.b)
print(s.calc(3))

print("SomeClass 3")
s = SomeClass3(1, 2)
print(s.a)
print(s.b)
print(s.calc(3))
print(type(c.__init__))
print(type(s))
print(type(type))
