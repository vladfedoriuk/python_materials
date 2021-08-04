import random
import math


# Numbers:

print("17/3 = ", 17 / 3)
print("17//3 = ", 17 // 3)
print("17%3 = ", 17 % 3)
print("5**2 = ", 5 ** 2)  # 5 to power of 2
print("2**7 = ", 2 ** 7)  # 2 to power of 7
print("pow(2, 7) = ", pow(2, 7))
print("round(1098.7654, 2) = ", round(1098.7654, 2))
print("abs(-1,.4) = ", abs(-1.4))
print("divmod(8 , 6) = ", divmod(8, 6))

x = 1  # int
y = 2.8  # float
z = 1j  # complex
t = complex(2, 3)
print("t = ", t)
print("t.conjugate() = ", t.conjugate())


# To verify the type of any object in Python, use the type() function:

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

x = 1
y = 35656222554887711
z = -3255522

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

x = 1.10
y = 1.0
z = -87.7e100

print(x, type(x))
print(y, type(y))
print(z, type(z))

# Complex types are written with a "j" as the imaginary part:

x = 3 + 5j
y = 5j
z = -5j

print(x, type(x))
print(y, type(y))
print(z, type(z))

# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a, type(a))
print(b, type(b))
print(c, type(c))

#!!!!!Note: You cannot convert complex types into another number type.

# Random types:

print(random.randrange(1, 10))

x = 9.8
print(x, math.trunc(x))
print(x, math.floor(x))
print(x, math.ceil(x))

x, y = 1, 2
print("x, y = {0}, {1}".format(x, y))
print(x | y)
print(x ^ y)
print(x & y)
print(x >> 2)
print(y << 2)
print(~x)
print(not (x < 5 and x < 10))

if isinstance(True, bool):
    print("is instance")

a = 10
b = 10
print(id(a) == id(b))
