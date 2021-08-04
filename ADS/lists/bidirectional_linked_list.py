class DoubleLinkedList(object):
    class Node(object):
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = self.tail = None
        self.size = 0

    def push_back(self, data):
        if not self.tail:
            self.head = self.tail = self.Node(data)
        else:
            p = self.Node(data)
            self.tail.next = p
            p.prev = self.tail
            self.tail = p
        self.size += 1

    def push_front(self, data):
        if not self.head:
            self.head = self.tail = self.Node(data)
        else:
            p = self.Node(data)
            self.head.prev = p
            p.next = self.head
            self.head = p
        self.size += 1

    def pop_back(self):
        if not self.tail:
            return None
        else:
            data = self.tail.data
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.size -= 1
            return data

    def pop_front(self):
        if not self.head:
            return None
        else:
            data = self.head.data
            self.head.next.prev = None
            self.head = self.head.next
            self.size -= 1
            return data

    def insert_after(self, node, data):
        if node is self.tail:
            self.push_back(data)
        else:
            p = self.Node(data)
            p.next = node.next
            node.next.prev = p
            p.prev = node
            node.next = p
            self.size += 1

    def insert_before(self, node, data):
        if node is self.head:
            self.push_front(data)
        else:
            p = self.Node(data)
            p.prev = node.prev
            node.prev.next = p
            p.next = node
            node.prev = p
            self.size += 1

    def remove_node(self, node):
        if node is self.head:
            self.pop_front()
        elif node is self.tail:
            self.pop_back()
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
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
