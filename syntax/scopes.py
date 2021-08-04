try:
    d = 2
    d()
except TypeError as e:
    print("is not a function", e)

print(callable(len), callable(2), callable(callable))

GLOBAL_VAR = 2


def f(n):
    print(GLOBAL_VAR, n)


def g(n):
    GLOBAL_VAR = 1
    print(GLOBAL_VAR, n)


def h(n):
    try:
        # GLOBAL_VAR += 1 # error (unresolved reference)
        print()
    except UnboundLocalError as e:
        print(e)
    pass


def t(n):
    print(OTHER_VAR, n)


OTHER_VAR = 3

GLOBAL_LIST = []


def d(n):
    GLOBAL_LIST.append(n)  # objects can bbe changed but not reassigned


f(1)
g(1)
t(1)
d(1)
print(GLOBAL_LIST)


def some_func(value):
    s = 23

    def fun():
        p = 12
        print("fun: ", OTHER_VAR, value, s, p)

    return fun


v = some_func(5)
v()
