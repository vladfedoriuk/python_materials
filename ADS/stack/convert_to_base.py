from .stack import Stack


def to_bin(number):
    stack = Stack()
    while number:
        stack.push(number % 2)
        number //= 2
    stack.collection.reverse()
    return "".join(map(str, stack.collection))


print(to_bin(12))
print(bin(12))


def base_converter(number, base):
    digits = "0123456789ABCDEF"
    stack = Stack()

    while number > 0:
        stack.push(number % base)
        number //= base

    stack.collection.reverse()
    return "".join(digits[i] for i in stack.collection)


print(base_converter(12, 2))
