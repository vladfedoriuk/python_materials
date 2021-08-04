import collections

# namedtuple
print("NamedTuple")
vision = (9.5, 8.8)
print(vision[0])
print(vision[1])

Vision = collections.namedtuple("Vis", ["left", "combined", "right"])
vision = Vision(9.5, 9.2, 8.8)
print(vision)
print(vision.left)
print(vision.right)
print(vision.combined)

print(vision[0])
print(vision[1])
print(vision[2])
print(vision._asdict())
print(vision._asdict()["left"], "\n")

point = collections.namedtuple("Point", ["x", "y"])
t = [11, 12]
p = point._make(t)
print(p)
print(p._replace(x=33))
print(p._fields)
d = {"x": 11, "y": 22}
print(point(**d))

Account = collections.namedtuple("Account", ["type", "balance"], defaults=[0])
print(Account._field_defaults)
print(Account("premium"))
print(Account(type="premium", balance=0))


class Point(collections.namedtuple("Point", ["x", "y"])):
    __slots__ = ()

    @property
    def dist(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return "point: x=%6.3f y=%6.3f dist=%6.3f" % (self.x, self.y, self.dist)


for p in Point(3, 4), Point(3.4, 1.2):
    print(p)

point3d = collections.namedtuple("Point3d", point._fields + ("z",))
p = point3d._make([1, 2, 3])
print(p)

# defaultdict
print("DefaultDict")
d = {}
d["age"] = d.get("age", 0) + 1
print(d)

d = {"age": 39}
d["age"] = d.get("age", 0) + 1
print(d)

dd = collections.defaultdict(int)
dd["age"] += 1
print(dd)
print(dd["height"])

s = [("a", 1), ("b", 2), ("a", 5), ("c", 9), ("b", 6)]
d = collections.defaultdict(list)
for key, val in s:
    d[key].append(val)
print(d)

d1 = {}
for key, val in s:
    d1.setdefault(key, []).append(val)
print(d1)

s1 = [("red", 1), ("red", 2), ("blue", 3), ("blue", 4), ("red", 1), ("blue", 3)]
d2 = collections.defaultdict(set)
for key, val in s1:
    d2[key].add(val)
print(d2)

import itertools_module


def constant_factory(value):
    return itertools_module.repeat(value).__next__


def constant_factory1(value):
    return lambda: value * 2


d3 = collections.defaultdict(constant_factory1(5))
d3.update(d=1, c=3)
print(d3[4])

# ChainMap
# is useful for providing defaults
# writes, updates, and deletions operate only on the first mapping

default_connection = {"host": "localhost", "port": 4567}
connection = {"port": 5678}
conn = collections.ChainMap(connection, default_connection)  # map creation

print(conn)
print(conn["port"])  # port is found in the first dictionary
print(conn["host"])  # host is found in the second dictionary
print(conn.maps)

conn["host"] = "google.com"
print(conn.maps)

del conn["port"]
print(conn.maps)
try:
    del conn["port"]
except KeyError:
    print("No key in the first mapping")  # the second mapping is immutable

print(conn["port"])

d = dict(conn)
print(d)

# Counter

print("\nCounter")
# collections.Counter([iterable-or-mapping])
cnt = collections.Counter()
for n in [1, 3, 2, 1, 2, 4, 4, 5, 3, 2, 1]:
    cnt[n] += 1
print(cnt)

words = (
    "A Counter is a dict subclass for counting hashable objects. It is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values. "
    "Counts are allowed to be any integer value including zero or negative counts. "
    "The Counter class is similar to bags or multisets in other languages.".split()
)

cnt = collections.Counter(words).most_common(5)
print(cnt)

c = collections.Counter()
print(c)
c = collections.Counter("abs")
print(c)
c = collections.Counter({"red": 4, "blue": 5})
print(c)
c = collections.Counter(a=3, b=4)
print(c)

c = collections.Counter([1, 2, 3])
print(c[4])

# Setting a count to zero does not remove an element from a counter. Use del to remove it entirely:
c[4] = 0
print(c)
del c[4]
print(c)

c = collections.Counter(a=4, b=2, c=0, d=-2)
print(list(c.elements()))

c = collections.Counter("algebra")
print(c.most_common(3))

c = collections.Counter(a=3, b=2, c=4, d=6)
d = collections.Counter(a=4, b=2, c=1, d=5)

# update([iterable-or-mapping]) subtract([iterable-or-mapping])

c.subtract(d)
print(c)

c.update("abcdef")
print(c)

# most common paterns on counter
sum(c.values())  # total of all counts
c.clear()  # reset all counts
list(c)  # list unique elements
set(c)  # convert to a set
dict(c)  # convert to a regular dictionary
c.items()  # convert to a list of (elem, cnt) pairs
collections.Counter(
    dict([(1, 3), ("a", 3), ("b", 4)])
)  # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
c += collections.Counter()  # remove zero and negative counts

# Mathematical operations

c = collections.Counter(a=3, b=1)
d = collections.Counter(a=1, b=2)
# c + d    add two counters together:  c[x] + d[x]
# c - d    subtract (keeping only positive counts)
# c & d    intersection:  min(c[x], d[x])
# c | d     union:  max(c[x], d[x])

print(c + d)
print(c - d)
print(c & d)
print(c | d)

# Deque
# collections.deque([iterable[,maxlen]])
d = collections.deque("ghi")
for elem in d:
    print(elem.upper(), end=", ")
print()

d.append("x")
d.appendleft("y")
print(d)

d.pop()
d.popleft()
print(d)

d = collections.deque(reversed(d))
print(d)

d.extend("abc")
print(d)

d.rotate(1)
print(d)
d.rotate(-1)
print(d)

d.clear()
try:
    d.pop()
except IndexError:
    print("nothing left in a deque")

d.extendleft("abc")
d.extend("efg")
print(d)

# OrederedDict
# collections.OrderedDict([items])
"An OrderedDict is a dict that remembers the order that keys were first inserted. " "If a new entry overwrites an existing entry, the original insertion position " "is left unchanged. Deleting an entry and reinserting it will move it to the end."

print("\nOrderedDict")
dct = {"banana": 3, "apple": 4, "pear": 1, "orange": 2}
orddict = collections.OrderedDict(dict(sorted(dct.items(), key=lambda t: t[0])))
print(orddict.items())
orddict = collections.OrderedDict(sorted(dct.items(), key=lambda t: t[1]))
print(orddict.items())

ordd = collections.OrderedDict()
ordd["b"] = 3
ordd["a"] = 1
ordd["c"] = 0
print(ordd)
"""
The popitem() method for ordered dictionaries returns and removes a (key, value) pair. 
The pairs are returned in LIFO order if last is true or FIFO order if false.
"""
p = ordd.popitem()
print(ordd)
print(p)
p = ordd.popitem(last=True)
print(ordd)
print(p)


class LastUpdatedDict(collections.OrderedDict):
    "Store elements in the order the keys were last added"

    def __setitem__(self, key, value):
        if key in self.keys():
            del self[key]
        collections.OrderedDict.__setitem__(self, key, value)


class OrderedCounter(collections.Counter, collections.OrderedDict):
    "Counter that remembers the order elements are first encountered"

    def __repr__(self):
        return "%s(%r)" % (self.__class__.__name__, collections.OrderedDict(self))

    def __reduce__(self):
        return self.__class__, (collections.OrderedDict(self),)
