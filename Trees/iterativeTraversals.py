from Tree import *


def preorderTraversal(root):

    if not root:
        return []

    res = []
    stack = []
    stack.append(root)

    while stack:
        top = stack.pop()
        res.append(top.val)

        if top.right:
            stack.append(top.right)

        if top.left:
            stack.append(top.left)

    return res


def inorderTraversal(root):
    if not root:
        return []

    stack = []
    res = []

    stack.append(root)
    curr = root
    while stack:
        if curr != None:
            stack.append(curr)
            curr = curr.left
        else:
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

    return res


def postorderTraversal(root):

    if not root:
        return []

    stack = []
    res = []

    stack.append(root)
    while stack:
        top = stack.pop()
        res.append(top.val)

        if top.left:
            stack.append(top.left)

        if top.right:
            stack.append(top.right)

    return reversed(res)
