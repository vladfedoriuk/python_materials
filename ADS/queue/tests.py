import unittest
from queue import Queue
from collections import deque


class QueueTest(unittest.TestCase):
    def test_empty(self):
        queue = Queue()
        self.assertTrue(queue.empty())
        queue.enqueue("1")
        queue.dequeue()
        self.assertTrue(queue.empty())

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(True)
        queue.enqueue(map)
        self.assertEqual(
            first=queue.collection, second=deque([1, True, map]), msg="enqueue failed"
        )

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(None)
        elem = queue.dequeue()
        self.assertEqual(first=elem, second=1, msg="dequeue retrieved wrong element")
        self.assertEqual(
            first=queue.collection,
            second=deque([None]),
            msg="inner collection is incorrect after dequeue",
        )

    def test_size(self):
        queue = Queue()
        queue.enqueue(True)
        queue.enqueue(None)
        queue.dequeue()
        queue.enqueue(False)
        self.assertEqual(first=queue.size(), second=2, msg="size is wrong")

    def test_head_tail(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.dequeue()
        queue.enqueue(3)
        self.assertEqual(first=queue.tail(), second=3, msg="tail is incorect")
        self.assertEqual(first=queue.head(), second=2, msg="head is incorect")
