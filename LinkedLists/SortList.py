from LinkedList import *


def sort(head):
    """
    Sort a linked list in O(nlog n) time.

    My approach: Merge sort
    """
    if not head or not head.next:
        return head
    elif not head.next.next:
        if head.val > head.next.val:
            s = head.next
            head.next.next = head
            head.next = None
            return s
        else:
            return head
    else:
        centerNode = findCenter(head)
        temp = centerNode.next
        centerNode.next = None
        one = sort(head)
        two = sort(temp)
        return merge(one, two)


def findCenter(head):

    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(headA, headB):
    dummy = LinkedListNode(-1)
    curr = dummy
    while headA != None and headB != None:
        if headA.val < headB.val:
            newNode = LinkedListNode(headA.val)
            headA = headA.next
        else:
            newNode = LinkedListNode(headB.val)
            headB = headB.next

        curr.next = newNode
        curr = newNode

    while headA != None:
        newNode = LinkedListNode(headA.val)
        curr.next = newNode
        curr = newNode
        headA = headA.next

    while headB != None:
        newNode = LinkedListNode(headB.val)
        curr.next = newNode
        curr = newNode
        headB = headB.next

    return dummy.next
