# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

this_set = {}
print(type(this_set))

this_set = set()
print(type(this_set))

this_set = {"apple", "banana", "orange"}
print(this_set)

for x in this_set:
    print(x)

print("banana" in this_set)

# Once a set is created, you cannot change its items, but you can add new items.

this_set.add("kiwi")
print(this_set)

this_set.update([1, 2, 3])
print(this_set)

print(len(this_set))
# If the item to remove does not exist, remove() will raise an error.
if "banana" in this_set:
    this_set.remove("banana")

# If the item to remove does not exist, discard() will NOT raise an error.
this_set.discard("banana")
if "kiwi" in this_set:
    this_set.discard("kiwi")
print(this_set)

# You can also use the pop(), method to remove an item, but this method will remove the last item.
# Remember that sets are unordered, so you will not know what item that gets removed.
# The return value of the pop() method is the removed item.

x = this_set.pop()
print(this_set)
print(x)

this_set.clear()
print(this_set)

del this_set

set1 = {1, 2, 3}
set2 = {"a", "b", "c"}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

# Both union() and update() will exclude any duplicate items.

set1 = set2.copy()

print("set1 = ", set1)
print("set3 = ", set3)
print("set3.difference(set1) = ", set3.difference(set1))
print(set1)
print(set3)
set3.difference_update(set1)
print("set3.difference_update(set1) = ", set3)

# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method,
# because the difference() method returns a new set, without the unwanted items,
# and the difference_update() method removes the unwanted items from the original set.

print("set1.intersection(set2) = ", set1.intersection(set2))
print(set1.isdisjoint(set2))
print(set1.issubset(set2))
print(set1.issuperset(set1))

# The issuperset() method returns True
# if all items in the specified set exists
# in the original set, otherwise it retuns False.

print(set3.symmetric_difference(set2))
print(set3.symmetric_difference_update(set2))
print(set3)
