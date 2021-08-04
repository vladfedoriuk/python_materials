a = []  # empty list
a = ["apple", "banana", "cherry"]

print(a)
print(a[1])
print(a[-1])
print(a[0:2])

a = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(a[-4:-1])

a[1] = "blackcurrant"
for item in a:
    print(item)

if "apple" in a:
    print("Apple is in a")

print(len(a))

a.append("pineapple")

print(a)

a.insert(2, "watermelon")
a.insert(len(a), "apple")

print(a)

if "apple" in a:
    a.remove("apple")

print(a)

a.pop(0)
a.pop()

print(a)

del a[3]

print(a)

a.clear()

print(a)

# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1,
# and changes made in list1 will automatically also be made in list2.

list1 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
a = list1.copy()
print(a)

a.clear()
print(a)

a = list(list1)
print(a)

list2 = [1, 2, 3]
list1 = a + list2
print(list1)

list1 = []
list1 = a
for x in list2:
    list1.append(x)

list1.extend(list2)
print(list1)

print(list1.count(1))

list1.insert(len(list1), "orange")
print(list1.index("orange"))
print(list1[4:].index("orange"))

list1.reverse()
print(list1)

# list1.sort()
# print(sorted(list1))
