class AttributesClass(object):
    def __init__(self, values):
        # self.values = values
        super(AttributesClass, self).__setattr__("values", values)

    def __getattr__(self, item):
        return self.values[item]

    def __setattr__(self, key, value):
        self.values[key] = value


"""
Python will call __getattr__ method whenever you request an attribute that hasn't already been defined.
"""


class AttributeManager(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __getattr__(self, item):
        super(AttributeManager, self).__setattr__(item, -1)
        return self.item


"""
 If you have __getattribute__ method in your class, 
 python invokes this method for every attribute regardless whether it exists or not.
 
 
Important: In order to avoid infinite recursion in __getattribute__ method, 
its implementation should always call the base class method with the same name to access any attributes it needs. 
For example: 
object.__getattribute__(self, name) or super().__getattribute__(item)

IMPORTANT
If your class contains both getattr and getattribute magic methods then __getattribute__ is called first. 
But if __getattribute__ raises AttributeError exception then the exception will be ignored
 and __getattr__ method will be invoked.
"""


class Data(object):
    def __init__(self, data):
        self.data = data

    def __getattribute__(self, item):
        print("__getattribute__ invocation")
        return super(Data, self).__getattribute__(item)

    def __getattr__(self, item):
        print("__getattr__ invocation")
        self.__setattr__(item, None)
        return self.item

    def __setattr__(self, key, value):
        super(Data, self).__setattr__(key, "value:" + str(value))


class ReadOnlyAttribute(object):
    def __init__(self, data):
        self.data = data

    def __get__(self, obj, obj_type=None) -> object:
        print("Retrieving value from __get__")
        print(f"obj: {obj}")  # returns Foo object
        print(f"obj_type: {obj_type}")  # returns Foo
        return self.data

    def __set__(self, obj, value) -> None:
        print("Setting value in __set__")
        print(f"obj: {obj}")  # returns Foo object
        print(f"value: {value}")  # returns 6 ( value to be assigned )
        raise AttributeError("Cannot assign value to this attribute")


class Foo(object):
    attr = ReadOnlyAttribute(42)
    # attr.__get__(Foo) == Foo.d


class PropertyExample(object):
    @property
    def attribute(self) -> object:
        return 42

    @attribute.setter
    def attribute(self, value: object) -> None:
        raise AttributeError("cannot assign value to an attribute")

    @attribute.deleter
    def attribute(self):
        del self


class EquivalentProperty(object):
    def getter(self):
        return 42

    def setter(self, value):
        raise AttributeError("cannot assign value to an attribute")

    attribute = property(getter, setter)
    # property(fget=None, fset=None, fdel=None, doc=None) -> object


class C(object):
    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = property(getx, setx, delx, "I'm the 'x' property.")


if __name__ == "__main__":
    attr = AttributesClass({"one": 1, "two": 2})
    attr.three = 3
    print(attr.three, attr.one)

    attr = AttributeManager(1, 2)
    print(attr.c)

    attr = Data("data")
    print(attr.c)

    f = Foo()
    print(f.attr)
    try:
        f.attr = 6
    except AttributeError as ae:
        print(f"Error: {ae}")

    p = PropertyExample()
    print(p.attribute)
    try:
        p.attribute = 6
    except AttributeError as ae:
        print(f"Error: {ae}")
    del p.attribute

    ep = EquivalentProperty()
    print(ep.attribute)
    try:
        p.attribute = 7
    except AttributeError as ae:
        print(f"Error: {ae}")

    c = C()
    c.x = 1
    print(c.x)
    del c.x
