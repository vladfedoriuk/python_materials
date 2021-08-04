import heapq
import functools


class MaxHeap(object):
    @functools.total_ordering
    class MaxHeapData(object):
        def __init__(self, data):
            self.data = data

        def __lt__(self, other):
            return self.data > other.data

        def __eq__(self, other):
            return self.data == other.data

        def __repr__(self):
            return f"<{self.data}>"

    def __init__(self, h=None):
        self.h = list(map(self.MaxHeapData, h)) if h else []
        heapq.heapify(self.h)

    def push(self, data):
        heapq.heappush(self.h, self.MaxHeapData(data))

    def pop(self) -> MaxHeapData:
        return heapq.heappop(self.h)

    def pushpop(self, data) -> MaxHeapData:
        return heapq.heappushpop(self.h, self.MaxHeapData(data))

    def replace(self, data) -> MaxHeapData:
        return heapq.heapreplace(self, self.MaxHeapData(data))

    def nlargest(self, n: int) -> list[MaxHeapData]:
        return heapq.nsmallest(n, self.h)

    def nsmallest(self, n: int) -> list[MaxHeapData]:
        return heapq.nlargest(n, self.h)

    def __getitem__(self, i):
        return self.h[i]


if __name__ == "__main__":
    heap = MaxHeap([1, 3, 2, 6, 4, 9, 8, 7])
    print(heap.pop())
    print(heap.pushpop(-1))
    heap.push(11)
    print(heap.nlargest(5))
    print(heap.nsmallest(5))
