#!/usr/bin/env python
# -*- coding: utf-8 -*-


class MyClass(object):
    def __new__(cls, x, y, z):
        print("constructing instance with arguments:")
        print("    ", cls, x, y, z)
        instance = super(MyClass, cls).__new__(cls)
        return instance

    def __init__(self, a, b, c):
        print("initializing instance with arguments:")
        print("    ", self, a, b, c)

        self.a = a
        self.b = b
        self.c = c


inst = MyClass(23, 42, "spam")


class Singleton(object):
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = super().__new__(cls)
            cls.instance.data = {}
        return cls.instance

    def __getitem__(self, item):
        return self.instance.data[item]

    def __setitem__(self, key, value):
        self.instance.data[key] = value

    def __str__(self):
        return "Singleton({})".format(self.instance.data)


s = Singleton()
print(s)
s[1] = 2
s[2] = 1
print(s)

s = Singleton()
print(s)
