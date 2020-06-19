class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def arrayToList(arr):
    dummy = LinkedListNode(-1)
    curr = dummy
    for element in arr:
        newNode = LinkedListNode(element)
        curr.next = newNode
        curr = newNode

    return dummy.next


def printLinkedList(head):
    res = ""
    while head != None:
        res += str(head.val) + " -> "
        head = head.next
    res += 'NULL'
    print(res)
