class Parent:
    def call(self):
        print("Parent")


class Child(Parent):
    def call(self):
        print("Child")


class Example(object):
    def call(self):
        print("Ex")


def call_obj(obj):
    obj.call()


call_obj(Parent())
call_obj(Child())
call_obj(Example())


class Obj:
    def __init__(self, s):
        self.s = s

    def __add__(self, other):
        return self.s + "+" + other.s


def sum_two_objects(one, two):
    return one + two


print(sum_two_objects(Obj("obj1"), Obj("obj2")))
print(sum_two_objects(1, 2))
