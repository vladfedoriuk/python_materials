class Parent:
    def __init__(self):
        print("Parent initialized")
        self.value = "Parent"

    def do(self):
        print("Parent do(): value: {}".format(self.value))


class Child(Parent):
    def __init__(self):
        print("Child initialized")
        self.value = "Child"


parent = Parent()
parent.do()

child = Child()
child.do()


class Calc:
    def __init__(self, number):
        self.number = number

    def calc_and_print(self):
        self.print_number(self.calc())

    def calc(self):
        return self.number * 10 + 2

    def print_number(self, value):
        print("Number: ", value)


c = Calc(3)
c.calc_and_print()


class CalcExtraValue(Calc):
    def calc(self):
        return self.number - 100


c1 = CalcExtraValue(3)
c1.calc_and_print()


class Test:
    pass


class Test(object):  # it is the same as the code above (py3 only)
    pass
