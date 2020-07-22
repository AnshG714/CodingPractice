"""
A simple LRU cache, implemented as a Doubly Linked List and HashMap
"""


class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = DLLNode("Dummy", "Head")
        self.tail = DLLNode("Dummy", "Tail")
        self.map = {}
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        if key in self.map:
            node = self.map[key]
            self.removeNode(node)
            self.insertNodeAtHead(node)
            return node.val
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            self.removeNode(self.map[key])

        newNode = DLLNode(key, value)
        self.insertNodeAtHead(newNode)

        if len(self.map) > self.capacity:
            del self.map[self.tail.prev.key]
            self.removeNode(self.tail.prev)

    def removeNode(self, node):
        node.prev.next, node.next.prev = node.next, node.prev

    def insertNodeAtHead(self, node):
        node.prev, node.next = self.head, self.head.next
        self.head.next = node.next.prev = node
