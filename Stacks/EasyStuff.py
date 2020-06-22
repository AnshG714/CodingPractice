from Stack import *


def removeOuterParens(s):
    """
    A valid parentheses string is either empty (""), "(" + A + ")", or A + B,
    where A and B are valid parentheses strings, and + represents string
    concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid
    parentheses strings.

    A valid parentheses string S is primitive if it is nonempty, and there does not
    exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

    Given a valid parentheses string S, consider its primitive decomposition:
    S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

    Return S after removing the outermost parentheses of every primitive string in
    the primitive decomposition of S.
    """
    stack = Stack()
    res = ""
    for c in s:
        if c == "(":
            if not stack.isEmpty():
                res += "("
            stack.push("(")
        else:
            stack.pop()
            if not stack.isEmpty():
                res += ")"

    return res


def makeStackOpsArray(target, n):
    """
    Given an array target and an integer n. In each iteration, you will read a 
    number from  list = {1,2,3..., n}.

    Build the target array using the following operations:

    Push: Read a new element from the beginning list, and push it in the array.
    Pop: delete the last element of the array.
    If the target array is already built, stop reading more elements.
    You are guaranteed that the target array is strictly increasing, only 
    containing numbers between 1 to n inclusive.

    Return the operations to build the target array.

    You are guaranteed that the answer is unique.

    Input: target = [1,3], n = 3
    Output: ["Push","Push","Pop","Push"]

    Input: target = [1,2,3], n = 3
    Output: ["Push","Push","Push"]
    """
    count = 1
    t_ind = 0
    res = []
    for num in target:
        while count < num:
            res.append("Push")
            res.append("Pop")
            count += 1

        count += 1
        res.append("Push")

    return res
