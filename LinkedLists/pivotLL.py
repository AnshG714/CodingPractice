from LinkedList import *


def pivotLL(head: LinkedListNode, k: int):
    """

    For any integer k, the pivot of a list of integers with respect to k is that 
    list with its nodes reordered so that all nodes containing keys less than k appear 
    before nodes containing k, and all nodes containing keys greater than k appear 
    after the nodes containing k.

    example: k = 7
    list = 3 -> 2 -> 2 -> 11 -> 7 -> 5 -> 11
    result: 3 -> 2 -> 2-> 5 -> 7 -> 11 -> 11
    """

    lessHead = LinkedListNode(-1)
    moreHead = LinkedListNode(-1)

    pl = lessHead
    pm = moreHead

    while head != None:
        if head.val < k:
            pl.next = head
            pl = pl.next
        else:
            pm.next = head
            pm = pm.next

        head = head.next

    printLinkedList(moreHead)
    printLinkedList(lessHead)

    pl.next = moreHead.next
    pm.next = None
    return lessHead.next
