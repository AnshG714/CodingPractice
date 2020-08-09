from collections import deque
from Tree import *


def levelTraversal(root):
    """
    Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

    For example:
    Given binary tree [3,9,20,null,null,15,7],

       3
      / \ 
     9  20
        / \ 
      15   7
    return its level order traversal as:

    [
      [3],
      [9,20],
      [15,7]
    ]
    """

    if not root:
        return []

    queue = deque()
    queue.append(root)
    res = []

    while queue:
        size = len(queue)
        temp = []

        for _ in range(size):
            top = queue.popleft()
            temp.append(top.val)

            if top.left:
                queue.append(top.left)

            if top.right:
                queue.append(top.right)

        res.append(temp)

    return res
