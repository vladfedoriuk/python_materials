GLOBAL_VALUE = 2


def do_work(value):
    return GLOBAL_VALUE * value + 2


def change_var(x):
    gl = globals()
    lc = locals()
    print("globals:\n", gl)
    print("locals:\n", lc)
    global GLOBAL_VALUE
    GLOBAL_VALUE = x


def change_var1(x):
    globals()["GLOBAL_VALUE"] = x


print(do_work(3))
change_var(3)
print(GLOBAL_VALUE)
change_var1(0)
print(GLOBAL_VALUE)


class Calc:
    def __init__(self, param):
        self.param = param

    def do_work(self, value):
        return self.param * value + 2

    def change_var(self, x):
        self.param = x
