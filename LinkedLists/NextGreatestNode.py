from LinkedList import *


def nextGreatestNode(head):
    """
    We are given a linked list with head as the first node.  Let's number the 
    nodes in the list: node_1, node_2, node_3, ... etc.

    Each node may have a next larger value: for node_i, next_larger(node_i) is 
    the node_j.val such that j > i, node_j.val > node_i.val, and j is the smallest 
    possible choice.  If such a j does not exist, the next larger value is 0.

    Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

    Note that in the example inputs (not outputs) below, arrays such as [2,1,5] 
    represent the serialization of a linked list with a head node value of 2, 
    second node value of 1, and third node value of 5.

    Example 1:

    Input: [2,1,5]
    Output: [5,5,0]

    Example 2:

    Input: [2,7,4,3,5]
    Output: [7,0,5,5,0]

    The idea is almost the same as nextGreatestElement (see dailyTemperatures in Stack)
    """

    stack = []
    res = [0] * length(head)
    p = 0

    while head != None:
        val = head.val
        while stack and stack[-1][0] <= val:
            _, index = stack.pop()
            res[index] = val

        stack.append((val, p))
        p += 1
        head = head.next

    return res


def length(head):
    count = 0
    while head != None:
        count += 1
        head = head.next

    return count
