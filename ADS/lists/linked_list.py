class LinkedList(object):
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def push_front(self, data: Node):
        if not self.head:
            self.head = self.tail = self.Node(data)
        else:
            new_node = self.Node(data)
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def push_back(self, data: Node):
        if not self.tail:
            self.head = self.tail = self.Node(data)
        else:
            new_node = self.Node(data)
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def pop_front(self):
        if not self.head:
            return None
        else:
            data = self.head.data
            self.head = self.head.next
            self.size -= 1
            return data

    def pop_back(self):
        if not self.tail:
            return None
        else:
            p = self.head
            while p.next.next:
                p = p.next
            data = p.next.data
            p.next = None
            self.size -= 1
            return data

    def insert_before(self, node: Node, data):
        if node is self.head:
            self.push_front(data)
        else:
            p = self.head
            while p.next is not node:
                p = p.next
            p.next = self.Node(data)
            p.next.next = node
            self.size += 1

    def insert_after(self, node: Node, data):
        if node is self.tail:
            self.push_back(data)
        else:
            p = self.head
            while p is not node:
                p = p.next
            p_next = p.next
            p.next = self.Node(data)
            p.next.next = p_next
            self.size += 1

    def remove_node(self, node: Node):
        if node is self.head:
            self.pop_front()
        elif node is self.tail:
            self.pop_back()
        else:
            k = self.head
            p = k.next
            while p is not node:
                p = p.next
                k = k.next
            k.next = p.next
            self.size -= 1

    def find(self, data):
        p = self.head
        while p:
            if p.data == data:
                return p
            p = p.next

    def remove(self, data):
        p = self.head
        while p:
            if p.data == data:
                k = p.next
                self.remove_node(p)
                p = k
            else:
                p = p.next

    def __str__(self):
        l = []
        p = self.head
        while p:
            l.append(p.data)
            p = p.next
        return l.__str__()
