from LinkedList import *


def add(headA, headB):
    dummy = LinkedListNode(-1)
    curr = dummy
    carry = 0
    while headA != None and headB != None:
        initVal = headA.val + headB.val + carry
        carry = initVal // 10
        newNode = LinkedListNode(initVal % 10)
        curr.next = newNode
        curr = newNode
        headA = headA.next
        headB = headB.next

    while headA != None:
        initVal = headA.val + carry
        carry = initVal // 10
        newNode = LinkedListNode(initVal % 10)
        curr.next = newNode
        curr = newNode
        headA = headA.next

    while headB != None:
        initVal = headB.val + carry
        carry = initVal // 10
        newNode = LinkedListNode(initVal % 10)
        curr.next = newNode
        curr = newNode
        headB = headB.next

    if carry == 1:
        curr.next = LinkedListNode(1)

    return dummy.next
