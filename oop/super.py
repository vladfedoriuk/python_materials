class Calc(object):
    def __init__(self, value):
        print("Calc constructor is called")
        self.value = value

    def count(self):
        print("calc")
        return self.value * 8 + 9


c = Calc(1.4)
print(c.count())


class DoubleCalc(Calc):
    def count(self):
        print("Double calc")
        return 2 * super().count()


c = DoubleCalc(1.4)
print(c.count())


class ExtendedCalc(DoubleCalc):
    def __init__(self, value, k=1):
        super().__init__(value)
        print("Extender", self.value)
        self.k = k

    def count(self):
        print("Extender calc")
        previous = super().count()
        return -1 * self.k * previous


e = ExtendedCalc(8, k=1.2)
print(e.count())

print(ExtendedCalc.__mro__)  # method resolution order
print()


class Rectangle(object):
    def area(self):
        print("area in Rectangle, self is ", self)
        return self.len * self.wid

    def __init__(self, len=0, wid=0):
        print("__init__ in Rectancle, self is ", self)
        self.len = len
        self.wid = wid

    def perimeter(self):
        print("perimeter in Rectangle")
        return 2 * (self.len + self.wid)


class Square(Rectangle):
    def __init__(self, len=0):
        print("__init__ in Square, self is ", self)
        super().__init__(len, len)

    def perimeter(self):
        print("perimeter in Square")
        return 4 * self.len


class Cube(Square):
    def __init__(self, l=0):
        print("__init__in Cube, self is ", self)
        super().__init__(l)

    def surface_area(self):
        ar = self.area()
        return 6 * ar

    def print_perim1(self):
        print("perim1: ", super().perimeter())

    def print_perim2(self):
        print("perim2 ", super(Square, self).perimeter())


s = Square(5)
print(s.area())
print(s.__dict__)
c = Cube(5)
print(c.__dict__)
c.print_perim1()
c.print_perim2()
print()


class Triangle:
    def __init__(self, base, height):
        print("__init__ in Triangle, self is ", self)
        self.base = base
        self.height = height

    def tri_area(self):
        print("area in Triangle, self is", self)
        return 0.5 * self.height * self.base


class RightPyramid(Square, Triangle):
    def __init__(self, len, p_height):
        print("__init__ in RightPyramid, self is ", self)
        super().__init__(len)
        self.p_height = p_height

    def area(self):
        print("area in RightPyramid, self is", self)
        base = super().area()
        perim = super().perimeter()
        return 0.5 * perim * self.p_height + base


p = RightPyramid(3, 5)
print(p.area())


class Pyramyd1(Square, Triangle):
    pass


class Pyramid2(Triangle, Square):
    pass


print("Pyramid1.__mro__ ", Pyramyd1.__mro__)
print("Pyramid2.__mro__ ", Pyramid2.__mro__)
