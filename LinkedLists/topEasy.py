from LinkedList import *


def deleteNode(node):
    """
    Write a function to delete a node (except the tail) in a singly linked list, 
    given only access to that node.
    """
    node.val = node.next.val
    node.next = node.next.next


def reverseLinkedListIterative(head):
    """
    Reverse a linked list iteratively
    """
    slow = None
    fast = head
    while fast != None:
        temp = fast.next
        fast.next = slow
        slow = fast
        fast = temp

    return slow


def reverseLinkedListRecursive(head):
    """
    recursive reversal
    """
    if not head or not head.next:
        return None

    tail = reverseLinkedListRecursive(head.next)
    head.next.next = head
    head.next = None

    return tail


def mergeTwoSortedLL(head1, head2):

    dummy = LinkedListNode(-1)  # dummy node
    curr = dummy
    while head1 != None and head2 != None:
        if head1.val < head2.val:
            nextNode = LinkedListNode(head1.val)
            head1 = head1.next
        else:
            nextNode = LinkedListNode(head2.val)
            head2 = head2.next

        curr.next = nextNode
        curr = nextNode

    while head1 != None:
        nextNode = LinkedListNode(head1.val)
        head1 = head1.next
        curr.next = nextNode
        curr = nextNode

    while head2 != None:
        nextNode = LinkedListNode(head2.val)
        head2 = head2.next
        curr.next = nextNode
        curr = nextNode

    return dummy.next
