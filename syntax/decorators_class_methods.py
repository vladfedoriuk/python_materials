from functools import wraps


def decorator(function):
    def inner(self, *args, **kwargs):
        s = function(self, *args, **kwargs)
        return "<p> {} </p>".format(s)

    return inner


def add_tag(tag):
    def tag_decorator(function):
        @wraps(function)
        def wrapper(self, *args, **kwargs):
            s = function(self, *args, **kwargs)
            return "<{0}> {1} </{0}>".format(tag, s)

        return wrapper

    return tag_decorator


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @decorator
    def get_age(self):
        return "age: {}".format(self.age)

    @add_tag("h1")
    def get_name(self):
        """'Return name of a person"""
        return "Name: {}".format(self.name)


p = Person("Alison", 29)
txt = p.get_age()
print(txt)
txt = p.get_name()
print(txt)
print(p.get_name.__module__)
print(p.get_name.__doc__)
print(p.get_name.__name__)
p1 = Person("Vlad", 19)
