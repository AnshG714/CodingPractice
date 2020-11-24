import math
class MinStack:
  def __init__(self):
    self.st = []

  def push(self, val):
    self.st.append((val, min(val, (self.st and self.st[-1][1]) or math.inf)))

  def pop(self):
    return self.st.pop()[0]

  def peek(self):
    return self.st[-1][0]

  def minEl(self):
    if self.st:
      return self.st[-1][1]
    return None