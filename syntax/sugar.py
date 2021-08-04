l = [x * x for x in [1, 2, 3, 4, 5, 6] if x % 2 == 0]
print(l)

print([(x, y) for x in range(1, 10) for y in range(1, x + 1)])


def work(value):
    return value * 2


m = map(work, [1, 2, 3])
print(m)
print(list(m))

f = filter(lambda x: x > 2, [1, -1, -2, 3, 4, 5])
print(f)
print(list(f))

from functools import reduce

res = reduce(lambda x, y: x * y, [1, 2, 3, 4, 5])
print(res)


def func(x: int, y: str) -> max(2, 9):
    pass


print(func.__annotations__)

d = {k: v for k, v in zip([1, 2, 3], ["a", "b", "c"])}
print(d)
