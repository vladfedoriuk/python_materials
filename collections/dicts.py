a = dict(A=-1, Z=1)
print(a)

b = {"A": -1, "Z": 1}
print(b)

c = dict(zip(["A", "Z"], [-1, 1]))
print(c)

d = dict([("A", -1), ("Z", 1)])
print(d)

e = dict({"A": -1, "Z": 1})
print(a == b == c == d == e)

ed = {**e, **d}  # merge two dicts
ed = e | d # python3.9+ only    
# is = whether objects have the same id, not only the value
print(list(zip(["h", "e", "l", "l", "o"], range(5))))
f = dict(list(zip(["h", "e", "l", "l", "o"], range(5))))
print(f)
print(d.keys())
print(d.values())
print(d.items())

print(f.popitem()) #  removes the last key-value pair added from d and returns it as a tuple:
#  d.popitem() raises a KeyError exception if d == {}
d = {'a': 1}
print(d.popitem())
try:
    print(d.popitem())
except KeyError:
    print('d is empty')
    
print(f.pop("l"))
try:
    f.pop("l")
except KeyError:
    print("already deleted")
f.pop("l", None) #If <key> is not in d, 
# and the optional <default> argument is specified, 
# then that value is returned, and no exception is raised

f.update({"another": "value"})
f.update(a=1)
print(f)
d.get("a")  # the same as d['a']
# but if the key is missing,
# no KeyError, returns None instead.
d.get("a", 177)  # default value is returned if the key is missing
print(d.get("b", 177))  # like this

g = {}
v = g.setdefault(
    "a", 1
)  # it behaves like get() but also sets the key with a given value if it is not there
print(v)
print(g)
g.setdefault("a", 2)
print(g)
g["a"] = 3
print(g)
g.pop("a")
print(g)
print(g.get("a"))

x = {}
x.setdefault("a", {}).setdefault("b", []).append(1)
print(x)

#Dict formatting
h = {}
h['word'] = 'garfield'
h['count'] = 42
s = 'I want %(count)d copies of %(word)s' % h  # %d for int, %s for string
  # 'I want 42 copies of garfield'
  
d = {'a':1, 'b':2, 'c':3}
del d['b']   ## Delete 'b' entry
try:
    del d['b']
except KeyError:
    print('d already deleted')
