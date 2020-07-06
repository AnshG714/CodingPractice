from collections import deque
from Tree import *


def serialize(root):
    if not root:
        return '[]'

    res = [root.val]
    queue = deque()
    queue.append(root)

    while queue:

        size = len(queue)

        for _ in range(size):
            top = queue.popleft()
            if top.left:
                queue.append(top.left)
                res.append(top.left.val)
            else:
                res.append(None)

            if top.right:
                queue.append(top.right)
                res.append(top.right.val)
            else:
                res.append(None)

    # trim Nones from the end
    p = len(res) - 1
    while res[p] == None:
        p -= 1

    return str(res[:p + 1])


def deserialize(string):
    if string == '[]':
        return None

    listEls = stringListToList(string)

    i = 1
    queue = deque()
    root = TreeNode(listEls[0])
    queue.append(root)
    while i < len(listEls):

        top = queue.popleft()

        if listEls[i] != "None":
            top.left = TreeNode(listEls[i])
            queue.append(top.left)

        i += 1

        if i >= len(listEls):
            break

        if listEls[i] != "None":
            top.right = TreeNode(listEls[i])
            queue.append(top.right)

        i += 1

    return root


def stringListToList(string: str):
    return string.strip("[]").replace(' ', '').split(',')
