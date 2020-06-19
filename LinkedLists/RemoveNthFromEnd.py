from LinkedList import *


def remove(head, n):
    """
    Given a linked list, remove the n-th node from the end of list and return its 
    head.
    o o o o o
    """
    slow = fast = head
    for _ in range(n):
        fast = fast.next

    if fast == None:
        return head.next

    while fast.next != None:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head
