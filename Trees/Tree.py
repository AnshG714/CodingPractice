from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        if not self:
            return "TreeNode { None }"

        return "TreeNode { val: " + str(self.val) + ", left: " + \
            self.left.__str__() + ", right: " + self.right.__str__() + "}"


def treeFromArray(arr):

    if arr[0] == None:
        return None

    i = 1
    queue = deque()
    root = TreeNode(arr[0])
    queue.append(root)

    while i < len(arr):
        top = queue.popleft()

        if arr[i]:
            top.left = TreeNode(arr[i])
        i += 1
        if arr[i]:
            top.right = TreeNode(arr[i])
        i += 1
        queue.append(top.left)
        queue.append(top.right)

    return root
