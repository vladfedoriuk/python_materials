import collections


class Person:
    def __init__(self, name=None, age=None):
        self.age = age
        self.name = name
        self.__known = collections.defaultdict(int)

    def know(self, person):
        self.__known[person] = 1

    def is_known(self, person):
        return bool(self.__known[person])


p1 = Person("Ander", 19)
p2 = Person("Vlad", 19)
p1.know(p2)
p2.know(p1)
print(p1.is_known(p2))
print(p2.is_known(p1))
print(p1.is_known(Person("Daniel", 20)))
