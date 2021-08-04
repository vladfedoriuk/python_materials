l = ["a", "b", "c"]
it = iter(l)
while True:
    try:
        el = next(it)
        print(el)
    except StopIteration:
        break

it = l.__iter__()
while True:
    try:
        el = it.__next__()
        print(el)
    except StopIteration:
        break
print(locals())
print(globals())

import itertools
import operator

"""
itertools.accumulate(iterable[, func])
Make an iterator that returns accumulated sums, or accumulated results of other binary functions (specified via the optional func argument). 
"""
l = [1, 2, 3]
print([x for x in itertools.accumulate(l)])
print([y for y in itertools.accumulate(l, func=operator.mul)])


def accumulate(iterable, func=operator.add):
    it = iter(iterable)
    total = 0
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for elem in it:
        total = func(total, elem)
        yield total


print([z for z in accumulate(["a", "b", "c"], operator.concat)])

"""
itertools.chain(*iterables)
Make an iterator that returns elements from the first iterable until it is exhausted, 
then proceeds to the next iterable, until all of the iterables are exhausted.
"""

print([x for x in itertools.chain(["a", "b", "c"], [1, 2, 3])])


def chain(*iterables):
    for it in iterables:
        for el in it:
            yield el


print([y for y in chain([1, 2, 3], ["a", "b", "c"])])

"""
class method chain.from_iterable(iterable)
Alternate constructor for chain(). Gets chained inputs from a single iterable argument that is evaluated lazily.
"""

print([x for x in itertools.chain.from_iterable(["abc", "def"])])


def from_iterable(iterable):
    for it in iterable:
        for el in it:
            yield el


print([y for y in from_iterable(["abc", "def"])])

"""
itertools.combinations(iterable, r)
Return r length subsequences of elements from the input iterable.
"""

print([x for x in itertools.combinations([1, 2, 3, 4], r=2)])


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.permutations(range(n), r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


print([y for y in combinations([1, 2, 3, 4], r=2)])

"""
itertools.combinations_with_replacement(iterable, r)
Return r length subsequences of elements from the input iterable allowing individual elements to be repeated more than once.
"""

print([x for x in itertools.combinations_with_replacement([1, 2, 3, 4, 5], r=2)])


def combinations_with_replacement(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    for indices in itertools.product(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)


print([y for y in combinations_with_replacement([1, 2, 3, 4, 5], r=2)])

"""
itertools.compress(data, selectors)
Make an iterator that filters elements from data returning only those that have a corresponding element 
in selectors that evaluates to True. 
Stops when either the data or selectors iterables has been exhausted. Roughly equivalent to:
"""

s = "ABCDEF"
selectors = [1, 1, 0, 1, 0, 0]
print([x for x in itertools.compress(s, selectors=selectors)])


def compress(s, selectors):
    return (d for d, s in zip(s, selectors) if s)


print([x for x in compress(s, selectors=selectors)])

"""
itertools.count(start=0, step=1)
Make an iterator that returns evenly spaced values starting with number start. 
Often used as an argument to map() to generate consecutive data points. 
Also, used with zip() to add sequence numbers. 
"""
cnt = itertools.count(10, 1)
for i in range(10):
    print(cnt.__next__(), end=" ")

print()


def count(start=0, step=1):
    n = start
    while True:
        yield n
        n += step


cnt = count(10, 1)
for i in range(10):
    print(cnt.__next__(), end=" ")

"""
itertools.cycle(iterable)
Make an iterator returning elements from the iterable and saving a copy of each.
When the iterable is exhausted, return elements from the saved copy. Repeats indefinitely. 
"""
print()
print([x for x, s in zip(itertools.cycle(s), range(len(s) * 2))])


def cycle(iterable):
    saved = []
    for element in iterable:
        yield element
        saved.append(element)
    while saved:
        for element in saved:
            yield element


print([x for x, s in zip(cycle(s), range(len(s) * 2))])

"""
itertools.groupby(iterable, key=None)
Make an iterator that returns consecutive keys and groups from the iterable. 
The key is a function computing a key value for each element. If not specified or is None, 
key defaults to an identity function and returns the element unchanged. 
Generally, the iterable needs to already be sorted on the same key function.
"""

data = "AAABBBSSSDDDRRREEEAAA"
groups = []
keys = []
for k, g in itertools.groupby(data):
    groups.append(list(g))
    keys.append(k)

print([(x, y) for x, y in zip(keys, groups)])

"""
itertools.dropwhile(predicate, iterable)
Make an iterator that drops elements from the iterable as long as the predicate is true; afterwards, returns every element.
"""

l = [1, 2, 3, 4, 5, 6]
print([x for x in itertools.dropwhile(lambda y: y < 4, l)])


def dropwhile(predicate, iterable):
    it = iterable.__iter__()
    for el in it:
        if not predicate(el):
            yield el
            break
    for el in it:
        yield el


print([x for x in dropwhile(lambda y: y < 4, l)])

"""
itertools.filterfalse(predicate, iterable)
Make an iterator that filters elements from iterable returning only those for which the predicate is False. 
If predicate is None, return the items that are false.
"""

l = [1, 3, 2, 5, 7, 6, 8, 9]
print([x for x in itertools.filterfalse(lambda y: y > 3, l)])


def filterfalse(predicate, iterable):
    if predicate is None:
        predicate = bool
    for x in iterable:
        if not predicate(x):
            yield x


print([x for x in filterfalse(lambda y: y > 3, l)])

"""
itertools.permutations(iterable, r=None)
Return successive r length permutations of elements in the iterable.
"""

l = [1, 2, 3, 4]
print([x for x in itertools.permutations(l, r=2)])


def permutations(iterable, r=None):
    pool = tuple(iterable)
    r = len(pool) if not r else r
    for indices in itertools.product(range(len(pool)), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[x] for x in indices)


print([x for x in permutations(l, r=2)])

"""
itertools.product(*iterables, repeat=1)
Cartesian product of input iterables.

Roughly equivalent to nested for-loops in a generator expression. 
For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
To compute the product of an iterable with itself, specify the number of repetitions 
with the optional repeat keyword argument. For example, product(A, repeat=4) means 
the same as product(A, A, A, A).
"""

print([(x, y, z) for (x, y, z) in itertools.product([1, 2, 3], repeat=3)])

"""
itertools.repeat(object[, times])
Make an iterator that returns object over and over again. Runs indefinitely unless the times argument is specified.
"""

print(list(map(pow, range(5), itertools.repeat(2))))


def repeat(object, times=None):
    if times is None:
        while True:
            yield object
    else:
        for i in range(times):
            yield object


print([x for x in map(pow, range(5), repeat(2))])

"""
itertools.starmap(function, iterable)
Make an iterator that computes the function using arguments obtained from the iterable. Used instead of map()
 when argument parameters are already grouped in tuples from a single iterable (the data has been “pre-zipped”). 
The difference between map() and starmap() parallels the distinction between function(a,b) and function(*c).
"""

print([y for y in itertools.starmap(pow, [(1, 2), (3, 4), (5, 6)])])


def starmap(function, iterable):
    for it in iterable:
        yield function(*it)


print([y for y in starmap(pow, [(1, 2), (3, 4), (5, 6)])])

"""
itertools.takewhile(predicate, iterable)¶
Make an iterator that returns elements from the iterable as long as the predicate is true.
"""

print([x for x in itertools.takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])])


def takewhile(predicate, iterable):
    for el in iterable:
        if predicate(el):
            yield el
        else:
            break


print([x for x in takewhile(lambda x: x < 5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])])

"""
itertools.islice(iterable, start, stop[, step])
Make an iterator that returns selected elements from the iterable. 
If start is non-zero, then elements from the iterable are skipped until start is reached. 
Afterward, elements are returned consecutively unless step is set higher than one which results in items being skipped. 
If stop is None, then iteration continues until the iterator is exhausted, if at all; otherwise, 
it stops at the specified position. 
"""

from itertools import islice

print(
    *islice("ABCDEFG", 2),
    "\n",
    *islice("ABCDEFG", 2, 4),
    "\n",
    *islice("ABCDEFG", 2, None),
    "\n",
    *islice("ABCDEFG", 0, None, 2),
)

"""
itertools.zip_longest(*iterables, fillvalue=None)
Make an iterator that aggregates elements from each of the iterables. If the iterables are of uneven length, 
missing values are filled-in with fillvalue. Iteration continues until the longest iterable is exhausted.
"""

print([x for x in itertools.zip_longest("ABC", [1, 2], "-", fillvalue=".")])


def zip_longest(*iterable, fillvalue=None):
    iterables = [iter(x) for x in iterable]
    nums_active = len(iterables)
    if not nums_active:
        return
    values = []
    while True:
        values.clear()
        for i, it in enumerate(iterables):
            try:
                value = it.__next__()
            except StopIteration:
                nums_active -= 1
                if not nums_active:
                    return
                value = fillvalue
                iterables[i] = itertools.repeat(fillvalue)
            values.append(value)
        yield tuple(values)


print([x for x in zip_longest("ABC", [1, 2], "-", fillvalue=".")])
