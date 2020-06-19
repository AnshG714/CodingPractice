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
    """
    Merge 2 sorted Linked Lists
    """
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


def checkIfLinkedListHasCycle(head):
    """
    Return true if linked list has a cycle, false otherwise. 

    Idea: Floyd's Hare and Tortoise Algorithm
    """
    hare = tortoise = head

    while hare != None and hare.next != None:
        if hare == tortoise:
            return True
        hare = hare.next.next
        tortoise = tortoise.next

    return False


def getListLength(head):
    acc = 0
    while head != None:
        head = head.next
        acc += 1

    return acc


def intersection(headA, headB):
    """
    Write a program to find the node at which the intersection of two singly 
    linked lists begins.

    Notes:
    - If the two linked lists have no intersection at all, return null.
    - The linked lists must retain their original structure after the function 
        returns.
    - You may assume there are no cycles anywhere in the entire linked structure.
    - Your code should preferably run in O(n) time and use only O(1) memory.

    My idea: 
    - First, record the lengths of the 2 lists
    - Move the pointer from longer list by abs(lenA - lenB)
        - Now, this means the pointers on both lists are the same distance away
          from the intersection, if there is any. 
    - Move the pointers on both lists one at a time, until the pointer is either
      None or they point to the same node. 
    """
    lenA = getListLength(headA)
    lenB = getListLength(headB)

    if lenA > lenB:
        headA, headB = headB, headA  # Ensure that the linked list with headA is shorter

    count = 0
    while count < abs(lenA - lenB):
        headB = headB.next
        count += 1

    while headA != None and headB != None:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None


def isPalindromeNaive(head):
    """
    Given a singly linked list, determine if it is a palindrome. 

    O(n) space
    """

    l = []
    while head != None:
        l.append(head.val)
        head = head.next

    p1, p2 = 0, len(l) - 1

    while p1 <= p2:
        if l[p1] != l[p2]:
            return False
        p1 += 1
        p2 -= 1

    return True


def isPalindrome(head):
    """
    Given a singly linked list, determine if it is a palindrome. 

    O(1) space. Reverse the second half of the list, and compare two halves
    """

    slow = fast = head
    if not head:
        return True

    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next

    ll = reverseLinkedListIterative(slow.next)
    slow.next = ll

    fast = slow.next
    slow = head

    while fast != None:
        if slow.val != fast.val:
            return False
        slow = slow.next
        fast = fast.next

    return True
