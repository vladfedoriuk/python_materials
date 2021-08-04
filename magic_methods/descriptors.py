"""
A descriptor that returns a constant
"""


class Ten(object):
    def __get__(self, obj, objtype=None):
        return 10


"""
To use descriptors, it must be stored as a class variable in another class
"""


class A(object):
    x = 5
    y = Ten()


"""
In the a.x attribute lookup, the dot operator finds the key x and the value 5 in the class dictionary. 
In the a.y lookup, the dot operator finds a descriptor instance, recognized by its __get__ method, 
and calls that method which returns 10.
Note that the value 10 is not stored in either the class dictionary or the instance dictionary. 
Instead, the value 10 is computed on demand.
"""

import os


class DirectorySize(object):
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory(object):

    size = DirectorySize()

    def __init__(self, dirname: str) -> None:
        self.dirname = dirname


import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess(object):
    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info("Accessing %r giving %r", "age", value)
        return value

    def __set__(self, obj, value):
        logging.info("Updating %r to %r", "age", value)
        obj._age = value


class Person(object):

    age = LoggedAgeAccess()  # Descriptor inctance initialization

    def __init__(self, name, age):
        self.name = name  # Regular instance attribute
        self.age = age  # Calls __set__()

    def birthday(self):
        self.age += 1  # calls both __get__() and __set__()


class LoggedAccess(object):
    def __set_name__(self, owner, name):
        self.public_name = name  # name of the descriptor in the owner class
        self.private_name = "_" + name  # name of the attribute in the owner class

    def __get__(self, obj, objtype=None):
        value = getattr(obj, self.private_name)
        logging.info("Accessing %r giving %r", self.public_name, value)
        return value

    def __set__(self, obj, value):
        logging.info("Updating %r to %r", self.public_name, value)
        setattr(obj, self.private_name, value)


class Person1(Person):
    name = LoggedAccess()
    age = LoggedAccess()


"""
Descriptors get invoked by the dot “operator” during attribute lookup. 
If a descriptor is accessed indirectly with vars(some_class)[descriptor_name], 
the descriptor instance is returned without invoking it.

Descriptors only work when used as class variables. When put in instances, they have no effect.
"""

from abc import ABC, abstractmethod


class Validator(ABC):
    def __set_name__(self, owner, name):
        self.private_name = "_" + name

    def __get__(self, obj, objtype=None):
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        self.validate(value)
        setattr(obj, self.private_name, value)

    @abstractmethod
    def validate(self, value):
        pass


"""
Custom validators need to inherit from Validator
and must supply a validate() method to test various restrictions as needed.
"""


class OneOf(Validator):
    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f"Expected{value} to be one of {self.options}")


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError(f"Expected {value}to be an into or float")

        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f"Expected {value} to be at least {self.minvalue}")
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f"Expected {value} to be no more than {self.maxvalue}")


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected {value} to be str")
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f"Expected {value} to be no smaller than {self.minsize}")
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f"Expected {value} to be no longer than {self.maxsize}")

        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f"Expected {self.predicate} to be true for {value}")


class Component(object):

    name = String(minsize=3, maxsize=10, predicate=str.isupper)
    kind = OneOf("wood", "metal", "plastic")
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity


"""
Descriptor protocol¶

descr.__get__(self, obj, type=None) -> value

descr.__set__(self, obj, value) -> None

descr.__delete__(self, obj) -> None
"""

"""
 __set__() or __delete__(), it is considered a data descriptor.
 only __get__() are called non-data descriptors. 
"""

"""
Data and non-data descriptors differ 
in how overrides are calculated with 
respect to entries in an instance’s dictionary.

If an instance’s dictionary has an entry with the same name as a data descriptor, 
the data descriptor takes precedence. If an instance’s dictionary
has an entry with the same name as a non-data descriptor, the dictionary entry takes precedence.
"""

"""
desc.__get__(obj) or desc.__get__(None, cls).
"""

"""
Invocation from an instance

Instance lookup scans through a chain of namespaces 
giving data descriptors the highest priority, 
followed by instance variables, then non-data descriptors, 
then class variables, and lastly __getattr__() if it is provided.

If a descriptor is found for a.x, then it is invoked with: desc.__get__(a, type(a)).

The logic for a dotted lookup is in object.__getattribute__(). Here is a pure Python equivalent:
"""


def object_getattribute(obj, name):
    null = object()
    objtype = type(obj)
    cls_var = getattr(objtype, name, null)
    descr_get = getattr(type(cls_var), "__get__", null)
    if descr_get is not null:
        if hasattr(type(cls_var), "__set__") or hasattr(type(cls_var), "__delete__"):
            return descr_get(cls_var, obj, objtype)
    if hasattr(obj, "__dict__") and name in vars(obj):
        return vars(obj)[name]
    if descr_get is not null:
        return descr_get(cls_var, obj, objtype)
    if cls_var is not null:
        return cls_var
    raise AttributeError(name)


def getattr_hook(obj, name):
    try:
        return obj.__getattribute__(name)
    except AttributeError as ae:
        if not hasattr(type(obj), "__getattr__"):
            raise ae
    return type(obj).__getattr__(obj, name)


if __name__ == "__main__":
    a = A()
    print("a.x", a.x)
    print("a.y", a.y)

    d = Directory("./")
    print("d.size", d.size)
    mary = Person("Mary  M", 30)
    dave = Person("David D", 30)

    print(vars(mary))
    print(vars(dave))

    print(mary.age)
    print(mary.birthday())

    print(dave.name, dave.age)

    print(vars(vars(Person1)["name"]))
    print(vars(vars(Person1)["age"]))

    pete = Person1("Peter P", 10)
    kate = Person1("Catherine C", 20)
