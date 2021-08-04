import unittest
from .linked_list import LinkedList
from .bidirectional_linked_list import DoubleLinkedList


class ListTest(unittest.TestCase):
    def check_list(self, list_cls):
        l = list_cls()
        l.push_back(1)
        l.push_front(2)
        l.push_back(3)
        self.assertEqual(first=str(l), second=str([2, 1, 3]))
        self.assertEqual(first=l.size, second=3)
        p = l.find(1)
        self.assertEqual(first=p.data, second=1)
        l.insert_after(p, -2)
        l.insert_before(p, -1)
        p = l.find(2)
        l.insert_before(p, 0)
        l.insert_after(p, -3)
        p = l.find(3)
        l.insert_after(p, 9)
        l.insert_before(p, 2)
        self.assertEqual(first=str(l), second=str([0, 2, -3, -1, 1, -2, 2, 3, 9]))
        self.assertEqual(first=l.size, second=9)
        l.remove(2)
        self.assertEqual(first=str(l), second=str([0, -3, -1, 1, -2, 3, 9]))
        self.assertEqual(first=l.size, second=7)
        l.pop_back()
        l.pop_front()
        self.assertEqual(first=str(l), second=str([-3, -1, 1, -2, 3]))
        self.assertEqual(first=l.size, second=5)

    def test_linked_list(self):
        self.check_list(LinkedList)

    def test_double_linked_list(self):
        self.check_list(DoubleLinkedList)
