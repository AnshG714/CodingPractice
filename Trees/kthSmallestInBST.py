from Tree import *


def kthSmallestInBST(root, k):
    """
    Given a BST, return it's k-th smallest element
    """

    inorder_list = inorder(root)
    return inorder_list[k - 1]


def inorder(root):
    if not root:
        return []

    return inorder(root.left) + [root.val] + inorder(root.right)
