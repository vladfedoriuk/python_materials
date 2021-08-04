class Car:
    pass


c = Car()
print(c, type(c))


# Classes can have variables called fields


class Room:
    number = "Room 34"
    floor = 4


r = Room()
r1 = Room()

print(r.number, r1.number, Room.number)
print(r.floor, r1.floor, Room.floor)

r.number = 12
r.floor = "5 floor"
print(r.number, r1.number, Room.number)
print(r.floor, r1.floor, Room.floor)

Room.number = 12
Room.floor = "5 floor"
print(r.number, r1.number, Room.number)
print(r.floor, r1.floor, Room.floor)


class Door:
    def open(self):
        print("self is", self)
        print("door is opened")
        self.opened = True


d = Door()
d.open()

c1 = Car()
try:
    print(c1.wheels)
except AttributeError as e:
    print("Error: ", e)
c1.wheels = "cool wheels"
print(c1.wheels)

c3 = c1
c1.seat = "cool seat"
print(c3.seat)
print(c1)
print(c3)

c.a = 3


class Window:
    is_open = False

    def open_close(self):
        self.is_open = not self.is_open
        print("Window is open: ", self.is_open)


w = Window()
w1 = Window()
print("Initial state: ", w.is_open, w1.is_open)
w.open_close()
print("Later state: ", w.is_open, w1.is_open)
print(Window.is_open)
Window.is_open = True  # is_open is a static class variable
print(Window.is_open)
w.open_close()
print("Further state: ", w.is_open, w1.is_open)


class TestClass:
    def __init__(self):
        print("Constructor is called")
        print("self is ", self)
        self.instance_variable = "smth"


t = TestClass()
t1 = TestClass()
print(t.instance_variable)


class Chair:
    def __init__(self, color):
        self.color = color


c = Chair("red")
print(c.color)

c.a = 3
print(c.a)
print(c.__dict__)
del c.a
try:
    print(c.a)
except AttributeError as e:
    print("Error: ", e)

print(c.__dict__)


class Test:
    pass


Test.a = 2
t = Test()
print(Test.a, t.a)
t.a = 1
print(Test.a, t.a)


class Demo:
    value = 3

    def __init__(self, i):
        self.i = i

    @staticmethod
    def count():
        print("value is", Demo.value)
        return "some"

    @classmethod
    def cls_count(cls):
        print("value is", cls.value)
        return cls.value

    @property
    def some(self):
        return "some"


p = Demo(2)
print(p.i)
print(Demo.value)
print(p.__class__.value)
print(Demo.count())
print(Demo.cls_count())
print(p.some)
