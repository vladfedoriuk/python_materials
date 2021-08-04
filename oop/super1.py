class Rectangle(object):
    def __init__(self, length, width, **kwargs):
        self.length = length
        self.width = width
        print()
        print("Rectangle__init__(), self is ", self)
        print("kwargs is ", kwargs)
        print("__dict__ is", self.__dict__)
        print()
        super().__init__(**kwargs)

    def area(self):
        print()
        print("In Rectangle area")
        print()
        return self.length * self.width

    def perimeter(self):
        print()
        print("In Rectangle perimeter")
        print()
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length, **kwargs):
        print()
        print("Square__init__(), self is ", self)
        print("kwargs is ", kwargs)
        print("__dict__ is", self.__dict__)
        print()
        super().__init__(length=length, width=length, **kwargs)


class Cube(Square):
    def surface(self):
        return 6 * self.area()

    def volume(self):
        return self.area() * self.length


class Triangle(object):
    def __init__(self, base, height, **kwargs):
        self.base = base
        self.height = height

        print()
        print("Triangle __init__(), self is ", self)
        print("kwargs is ", kwargs)
        print("__dict__ is", self.__dict__)
        print()

        super().__init__(**kwargs)

    def area(self):
        print()
        print("In Triangle area")
        print()
        return 0.5 * self.base * self.height


class RightPyramid(Square, Triangle):
    def __init__(self, base, slant_height, **kwargs):
        self.base = base
        self.slant_height = slant_height
        kwargs["height"] = slant_height
        kwargs["length"] = base
        kwargs["base"] = base

        print()
        print("RightPyramid __init__(), self is ", self)
        print("kwargs is ", kwargs)
        print("__dict__ is", self.__dict__)
        print()

        super().__init__(**kwargs)

    def area(self):
        print()
        print("In RightPyramid area")
        print()
        base_area = super().area()
        face_area = 0.5 * super().perimeter() * self.slant_height
        return face_area + base_area

    def area_2(self):
        face_area = (
            4 * super(Rectangle, self).area()
        )  # after Rectangle it goes to Triangle
        base_area = super().area()
        return face_area + base_area


rp = RightPyramid(1, 2)
print(rp.area())
print(rp.area_2())


class Root:
    def draw(self):
        # the delegation chain stops here
        assert not hasattr(super(), "draw")


class Shape(Root):
    def __init__(self, shapename, **kwds):
        self.shapename = shapename
        super().__init__(**kwds)

    def draw(self):
        print("Drawing.  Setting shape to:", self.shapename)
        super().draw()


class ColoredShape(Shape):
    def __init__(self, color, **kwds):
        self.color = color
        super().__init__(**kwds)

    def draw(self):
        print("Drawing.  Setting color to:", self.color)
        super().draw()


cs = ColoredShape(color="blue", shapename="square")
cs.draw()
