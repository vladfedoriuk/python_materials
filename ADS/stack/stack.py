from collections import deque


class Stack(object):
    def __init__(self):
        self.collection = deque()

    def push(self, x):
        self.collection.append(x)

    def peek(self):
        return self.collection[-1]

    def pop(self):
        return self.collection.pop()

    def empty(self):
        return len(self.collection) == 0

    def size(self):
        return len(self.collection)
