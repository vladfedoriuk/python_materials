from collections import Counter


class Basket:
    def __init__(self):
        self.__capacities = {}
        self.__cntr = Counter()
        self.__objects = []

    def set_capacity(self, obj, capacity):
        self.__capacities[obj.__class__] = capacity

    def put_object(self, obj):
        if self.__cntr[obj.__class__] + 1 <= self.__capacities[obj.__class__]:
            self.__objects.append(obj)
            self.__cntr[obj.__class__] += 1
        else:
            raise OverflowError("exceeded capacity")


class Bag:
    def __init__(self, capacity):
        self.capacity = capacity
        self.__objects = []

    def put_object(self, obj):
        if self.__objects.__len__() + 1 <= self.capacity:
            self.__objects.append(obj)
        else:
            raise OverflowError("exceeded capacity")


class Item:
    def put_in_container(self, container):
        container.put_object(self)


basket = Basket()
basket.set_capacity(Item(), 2)
basket.put_object(Item())
basket.put_object(Item())
try:
    basket.put_object(Item())
except OverflowError as e:
    print(e)
try:
    basket.put_object(Item())
except OverflowError as e:
    print(e)
