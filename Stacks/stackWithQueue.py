from collections import deque


class Stack:
    def __init__(self):
        self.top = None
        self.addQueue = deque()
        self.removeQueue = deque()

    def push(self, el):
        self.top = el
        self.addQueue.append(el)

    def pop(self):
        while len(self.addQueue) > 1:
            if len(self.addQueue) == 2:
                self.top = self.addQueue[-2]
            self.removeQueue.append(self.addQueue.popleft())

        l = self.addQueue.popleft()
        if len(self.removeQueue) == 0:
            self.top = None
        self.addQueue, self.removeQueue = self.removeQueue, self.addQueue
        return l

    def peek(self):
        return self.top

    def isEmpty(self):
        return len(self.addQueue) == 0 and len(self.removeQueue) == 0
