import math


def a(x):
    return math.acos((26.25 + x ** 2) / ((689.0625 + 116.5 * (x ** 2) + x ** 4) ** 0.5))


x = 0
temp = a(x)
delta = 0.01
while a(x + delta) > temp:
    temp = a(x + delta)
    x += delta

print(x)
