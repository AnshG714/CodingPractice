# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

"""
104. Maximum Depth of Binary Tree

Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

"""
def maxDepth(root):

    if root == None:
        return 0

    if root.left == None and root.right == None:
       return 1

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


from collections import *
def serial(root):
    mainList = []

    queue = deque()

    queue.append(root.val)

    print(root)

    while queue:
        
        queue.appendleft(root.val)

        queue.append(root.left)

        queue.append(root.right)

        root = queue.popleft()

        mainList.append(root)

    return str(mainList)

        

        

def serialize(root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        
        queue = deque()
        queue.append((root, 0))
        
        res = root.val
        level = 1
        while queue:
            lst = ["."] * (2 ** level)
            nonNull = 0
            for i in range(2 ** level):
              if queue:
                top = queue.popleft()
                lst[top[1]] = top[0].val

                if top[0].left:
                  queue.append((top[0].left, i))
                  nonNull += 1

                if top[0].right:
                  queue.append((top[0].right, i))
                  nonNull += 1

            if nonNull == 0:
              break

            res += ' '.join(lst)
            level += 1
            
        return res