import random


def ran():
    while True:
        yield random.random()


def my_range(end, start=0, step=1):
    yield start
    while start + step < end:
        yield start + step
        start += step


def my_map(func, iterable):
    for elem in iterable:
        yield func(elem)


def my_enumerate(iterable):
    i = 0
    for it in iterable:
        yield i, it
        i += 1


def my_zip(*iterables):
    l = [iter(x) for x in iterables]
    while True:
        try:
            yield tuple([next(y) for y in l])
        except StopIteration:
            break


def gen_from():
    yield from range(5)


if __name__ == "__main__":

    for x, y, z in my_zip([1, 2, 3], ["a", "b", "c"], [{}, None, []]):
        print(x, y, z)

    for i, el in my_enumerate(["a", "b", "c"]):
        print(i, el)

    print(list(my_map(sum, [[1, 2]])))

    for i in my_range(10):
        print(i, end=" ")
    print()

    print([x for x, _ in zip(ran(), range(10))])
    print([x for x in gen_from()])
