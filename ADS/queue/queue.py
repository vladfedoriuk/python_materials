from collections import deque


class Queue(object):
    def __init__(self):
        self.collection = deque()

    def enqueue(self, elem):
        self.collection.append(elem)

    def dequeue(self):
        return self.collection.popleft()

    def size(self):
        return len(self.collection)

    def empty(self):
        return len(self.collection) == 0

    def head(self):
        return self.collection[0]

    def tail(self):
        return self.collection[-1]
