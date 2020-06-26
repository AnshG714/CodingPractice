from Stack import *


def decodeString(s):
    """
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the 
    square brackets is being repeated exactly k times. Note that k is guaranteed 
    to be a positive integer.

    You may assume that the input string is always valid; No extra white spaces, 
    square brackets are well-formed, etc.

    Furthermore, you may assume that the original data does not contain any digits 
    and that digits are only for those repeat numbers, k. For example, there won't 
    be input like 3a or 2[4].
    """
    stack = Stack()

    for c in s:
        if c != ']':
            stack.push(c)
        else:
            # Get the contents between the brackets
            curr = ""
            while stack.peek() != '[':
                curr = stack.pop() + curr

            # Now, pop the [
            stack.pop()

            # Get all the digits
            times = ""
            while not stack.isEmpty() and stack.peek().isdigit():
                times = stack.pop() + times

            newSt = curr * int(times)
            stack.push(newSt)

    res = ""
    while not stack.isEmpty():
        res = stack.pop() + res

    return res
