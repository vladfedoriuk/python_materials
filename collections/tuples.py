this_tuple = ()
print(this_tuple)
this_tuple = ("apple", "banana", "cherry")
print(this_tuple)
print(this_tuple[2])
print(this_tuple[-2])
this_tuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

# The search will start at index 2 (included) and end at index 5 (not included).
print(this_tuple[2:4])
print(this_tuple[-4:-1])

# Once a tuple is created, you cannot change its values.
# Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround.
# You can convert the tuple into a list,
# change the list, and convert the list back into a tuple.

x = (1, 2, 3)
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

for x in this_tuple:
    print(x)

if "apple" in this_tuple:
    print("Apple is in this tuple")

print("tuple length is: ", len(this_tuple))

thistuple = ("apple",)
print(type(thistuple))

thistuple = "apple"
print(type(thistuple))

del x

t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = t1 + t2
print(t3)
thistuple = tuple((1, 2, 3, 4))
print(thistuple)

thistuple = thistuple + (2, 3, 4, 5)
print(thistuple.count(2))
print(thistuple.index(2))
