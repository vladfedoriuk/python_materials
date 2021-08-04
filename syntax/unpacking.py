s, k = (1, 2)
print(s, k)
s, *k = (1, 2, 3, 4)
print(s, k)
s, *k, p = "abcdefhg"
print(s, k, p)


def accept_args(*args):
    return sum(args)


print(accept_args(1, 2, 3))
try:
    print(accept_args([1, 2, 3]))
except TypeError as e:
    print("Error: ", e)

vals = [1, 2, 3]
print(accept_args(*vals))

d = {"a": 1, "b": 2}
print(*d)


def accept_kwargs(**kwargs):
    print(d.items())


accept_kwargs(a=1, b=2)


def experiment(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


experiment(a=1, b=2)
