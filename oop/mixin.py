class Rectangle:
    def __init__(self, lenght, width):
        print("Rectangle __init__")
        self.length = lenght
        self.width = width

    def area(self):
        print("Rectangle area")
        return self.length * self.width


class Triangle:
    def __init__(self, base, height):
        print("Triangle __init__")
        self.base = base
        self.height = height

    def area(self):
        print("Triangle area")
        return 0.5 * self.base * self.height


class VolumeMixin:
    def volume(self):
        return self.area() * self.p_height


class Prism(Rectangle, VolumeMixin):
    def __init__(self, length, width, height):
        print("Prism __init__")
        super().__init__(length, width)
        self.p_height = height


class TrianglePrism(Triangle, VolumeMixin):
    def __init__(self, base, height, p_height):
        print("TrianglePrism __init__")
        super().__init__(base, height)
        self.p_height = p_height


p = Prism(1, 2, 3)
print(p.volume())

t = TrianglePrism(1, 2, 3)
print(t.volume())
