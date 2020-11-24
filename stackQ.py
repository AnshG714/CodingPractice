class StackWithQueues:
  def __init__(self):
    self.frontStack = []
    self.backStack = []

  def isEmpty(self):
    return (not self.frontStack and not self.backStack) 

  def add(self, val):
    self.backStack.append(val)

  def peek(self):
    if self.frontStack: # equivalent to !self.frontStack.isEmpty();
      return self.frontStack[-1]

    while self.backStack:
      self.frontStack.append(self.backStack.pop())

    return self.frontStack[-1]

  def remove(self):
    if self.frontStack: # equivalent to !self.frontStack.isEmpty();
      return self.frontStack.pop()[-1]

    while self.backStack:
      self.frontStack.append(self.backStack.pop())

    return self.frontStack.pop()[-1]
