class MinStack:

  def __init__(self):
    self.st = []
    ## Every element of the stack is a tuple (a, b), where a is the topmost
    ## element in the normal stack, and b is the minimum element that the stack
    ## has seen UNTIL now. 

    # [4, 3, 2, 5]
    # [(4, 4), (3, 3), (2, 2), (5, 2)]

  def push(self, val):
    # if self.st != []:
    #   minVal = self.st[-1][1]
    # else:
    #   minVal = val
    self.st.append(
      (val, min(val, (self.st and self.st[-1][1]) or val ))
      )

  def pop(self):
    return self.st.pop()[0]

  def minEl(self):
    return self.st[-1][1]