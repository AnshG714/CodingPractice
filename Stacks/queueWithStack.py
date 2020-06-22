from Stack import *


class Queue:

    def __init__(self):
        self.addStack = Stack()
        self.removeStack = Stack()

    def push(self, el):
        self.addStack.push(el)

    def pop(self):
        if self.removeStack.isEmpty():
            while not self.addStack.isEmpty():
                self.removeStack.push(self.addStack.pop())

        return self.removeStack.pop()

    def peek(self):
        if self.removeStack.isEmpty():
            while not self.addStack.isEmpty():
                self.removeStack.push(self.addStack.pop())

        return self.removeStack.peek()

    def isEmpty(self):
        return self.addStack.isEmpty() and self.removeStack.isEmpty()
