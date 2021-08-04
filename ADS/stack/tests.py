import unittest
from .stack import Stack
from .balanced_parentheses import balanced_general, balanced_parentheses
from collections import deque


class StackTest(unittest.TestCase):
    def test_empty(self):
        stack = Stack()
        self.assertEqual(first=stack.empty(), second=True, msg="stack should be empty")
        self.assertEqual(
            first=stack.collection, second=deque([]), msg="list should be empty"
        )

    def test_push(self):
        stack = Stack()
        stack.push(4)
        stack.push("dog")
        stack.push(True)

        self.assertEqual(
            first=stack.collection,
            second=deque([4, "dog", True]),
            msg="lists are not equal after push",
        )

    def test_size(self):
        stack = Stack()
        stack.push(None)
        self.assertFalse(stack.empty())
        self.assertEqual(first=stack.size(), second=1, msg="stack has wrong size")

    def test_peek(self):
        stack = Stack()
        stack.push(123)
        self.assertEqual(first=stack.peek(), second=123, msg="peek is wrong")

    def test_pop(self):
        stack = Stack()
        stack.push(123)

        x = stack.pop()
        self.assertEqual(first=x, second=123, msg="pop is not correct")


class TestBalanced(unittest.TestCase):
    def test_balanced(self):
        self.assertTrue(balanced_parentheses("(())"))
        self.assertFalse(balanced_parentheses("(()"))
        self.assertFalse(balanced_parentheses(")"))
        self.assertTrue(balanced_parentheses(""))

    def test_general(self):
        self.assertFalse(balanced_general("({]"))
        self.assertTrue(balanced_general("([{}])"))
        self.assertTrue(balanced_general(""))
        self.assertFalse(balanced_general(")]{"))


if __name__ == "__main__":
    unittest.main()
