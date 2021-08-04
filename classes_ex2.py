class Figure:
    def print_data(self, *args):
        print(self.__class__, self.calc_len(*args))
        print(self.__class__, self.calc_area(*args))


class Triangle(Figure):
    def __init__(self, a=0, b=0, c=0):
        self.a = a
        self.b = b
        self.c = c

    def calc_area(self, a, b, c):
        if c < a + b and a < b + c and c < a + b:
            p = (a + b + c) / 2
            return (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return None

    def calc_len(self, a, b, c):
        if c < a + b and a < b + c and c < a + b:
            return a + b + c
        return None


class Square(Figure):
    def __init__(self, a=0):
        self.a = a

    def calc_len(self, a):
        return a * 4

    def calc_area(self, a):
        return a ** 2


class Rectangle(Figure):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def calc_len(self, a, b):
        return (a + b) * 2

    def calc_area(self, a, b):
        return a * b


args = list(map(int, input().split()))
if len(args) == 1:
    s = Square(1)
    s.print_data(*args)
if len(args) == 2:
    s = Rectangle()
    s.print_data(*args)
if len(args) == 3:
    s = Triangle()
    s.print_data(*args)

figures = [Square(), Rectangle(), Triangle()]
data = [[1], (1, 2), (3, 4, 5)]
print("list:")
[x.print_data(*args) for x, args in zip(figures, data)]
