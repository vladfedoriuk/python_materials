from collections import deque


class BST(object):
    class Node(object):
        def __init__(self, data, left=None, right=None, up=None):
            self.data = data
            self.left = left
            self.right = right
            self.up = up

        def __repr__(self):
            return f"<Node {self.data}>"

    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = self.Node(data)
            return True
        else:
            p = self.root
            while True:
                if p:
                    if data < p.data:
                        if p.left:
                            p = p.left
                            continue
                        else:
                            p.left = self.Node(data, up=p)
                            break
                    elif data > p.data:
                        if p.right:
                            p = p.right
                            continue
                        else:
                            p.right = self.Node(data, up=p)
                            break
                    else:
                        return False
                else:
                    return False
            return True

    @property
    def min(self) -> Node:
        p = self.root
        while p.left:
            p = p.left
        return p

    @property
    def max(self) -> Node:
        p = self.root
        while p.right:
            p = p.right
        return p

    def find(self, data) -> Node:
        p = self.root
        while p and not p.data == data:
            p = p.right if data > p.data else p.left
        return p

    def find_successor(self, node: Node) -> Node:
        if node.right:
            p = node.right
            while p.left:
                p = p.left
            return p
        else:
            p = node
            while p:
                if p.up and p.up.left == p:
                    p = p.up
                    break
                p = p.up
            return p

    def find_predeccessor(self, node: Node) -> Node:
        if node.left:
            p = node.left
            while p.right:
                p = p.right
            return p
        else:
            p = node
            while p:
                if p.up and p.up.right == p:
                    p = p.up
                    break
                p = p.up
            return p

    @staticmethod
    def __traverse_post_order(node: Node, func: callable):
        if node:
            BST.__traverse_post_order(node.left, func)
            BST.__traverse_post_order(node.right, func)
            func(node)

    @staticmethod
    def __traverse_pre_order(node: Node, func: callable):
        if node:
            func(node)
            BST.__traverse_pre_order(node.left, func)
            BST.__traverse_pre_order(node.right, func)

    @staticmethod
    def __traverse_in_order(node: Node, func: callable):
        if node:
            BST.__traverse_in_order(node.left, func)
            func(node)
            BST.__traverse_in_order(node.right, func)

    def __traverse_in_order_iterative(self, func: callable):
        node = self.root
        stack = deque()
        while node or not len(stack) == 0:
            if node:
                stack.appendleft(node)
                node = node.left
            else:
                node = stack.popleft()
                func(node)
                node = node.right

    def __traverse_pre_order_iterative(self, func: callable):
        node = self.root
        stack = deque()
        stack.appendleft(node)
        while not len(stack) == 0:
            node = stack.popleft()
            func(node)
            if node.right:
                stack.appendleft(node.right)
            if node.left:
                stack.appendleft(node.left)

    def delete_node(self, node: Node):

        if not node.left and not node.right:
            if node.up and node.up.left is node:
                node.up.left = None
            if node.up and node.up.right is node:
                node.up.right = None
            if not node.up:
                self.root = None

        elif node.left and not node.right:
            if node.up:
                if node.up.right is node:
                    node.up.right = node.left
                else:
                    node.up.left = node.right
            node.left.up = node.up
            if not node.left.up:
                self.root = node.left

        elif node.right and not node.left:
            if node.up:
                if node.up.right is node:
                    node.up.right = node.right
                else:
                    node.up.left = node.right
                node.right.up = node.up
            if not node.right.up:
                self.root = node.right

        else:
            succ = self.find_successor(node)
            if succ:
                node.data = succ.data
                self.delete_node(succ)

    def bfs(self, func: callable):
        queue = deque()
        queue.appendleft(self.root)
        while not len(queue) == 0:
            node = queue.pop()
            func(node)
            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

    def in_order(self, func: callable):
        self.__traverse_in_order_iterative(func)


if __name__ == "__main__":
    tree = BST()
    tree.insert(3)
    tree.insert(1)
    tree.insert(5)
    tree.insert(2)
    tree.insert(1.5)
    tree.insert(2.5)
    print(tree.max)
    print(tree.min)
    p = tree.find(3)
    print(p)
    print(tree.find_successor(p))
    tree.in_order(print)
    tree.delete_node(tree.find(1))
    print("after delete")
    tree.in_order(print)
    print("pred: ", tree.find_predeccessor(tree.find(2.5)))
    tree.bfs(print)
