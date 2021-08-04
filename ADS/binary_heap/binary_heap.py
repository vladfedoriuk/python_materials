import heapq


def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


h = []
heapq.heappush(h, (5, "write code"))
heapq.heappush(h, (7, "release product"))
heapq.heappush(h, (1, "write spec"))
heapq.heappush(h, (3, "create tests"))

print(heapq.heappop(h))  # (1, 'write spec')


h1 = [3, 9, 5, 1]
heapq.heapify(h1)  # transforms h1 into min-heap in linear time
print(h1[0])  # 1
print(heapq.heappop(h1))  # 1 and gets removed
heapq.heappush(h1, -1)
print(h1)  # -1 3 5 9
print(
    heapq.heappushpop(h1, 2)
)  # returns: -1, inserts 2, more efficient than heappush & heappop
print(h1)  # 2 3 5 9
print(
    heapq.heapreplace(h1, 4)
)  # returns: 2, inserts 4, more efficient than heappop & heappush. \
# InedexError if empty
print(h1)  # 3 4 5 9


print(
    next(heapq.merge([1, 3, 5], [2, 4, 6], [7, 8, 9], key=int, reverse=False))
)  # sorted(itertools.chain(*iterables))
# returns an iterable, ( Returns an iterator over the sorted values.)
# does not pull the data into memory all at once,
# and assumes that each of the input streams is already sorted (smallest to largest).
# To achieve behavior similar to sorted(itertools.chain(*iterables), reverse=True),
# all iterables must be sorted from largest to smallest.

h2 = [2, 3, 6, 3, 6, 7, 4, 9]
heapq.heapify(h2)
print(heapq.nlargest(5, h2))  # 9 7 6 6 4
print(heapq.nsmallest(5, h2))  # 2 3 3 4 6

# For max heaps:
heapq._heapify_max
heapq._heappop_max
heapq._heapreplace_max
# heapq._heappush_max - undocumented
# heapq._heappushpop_max - undocumented

if __name__ == "__main__":
    print(heapsort([9, 5, 6, 7, 2, 3, 9, 4, 5]))
