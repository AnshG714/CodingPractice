import sys
sys.path.insert(0, '../LinkedLists/')

from LinkedList import LinkedListNode


class EmptyStack(Exception):
    pass


class Stack:
    def __init__(self):
        self.head = None

    def push(self, element):
        if self.head is None:
            self.head = LinkedListNode(element)
        else:
            temp = self.head
            self.head = LinkedListNode(element)
            self.head.next = temp

    def pop(self):
        if self.head is None:
            raise EmptyStack
        else:
            temp = self.head
            self.head = self.head.next
            return temp.val

    def peek(self):
        if self.head is None:
            raise EmptyStack
        else:
            return self.head.val

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        res = "["
        curr = self.head
        while curr != None:
            if curr.next != None:
                res += str(curr.val) + ", "
            else:
                res += str(curr.val)
            curr = curr.next

        res += "]"
        return res
