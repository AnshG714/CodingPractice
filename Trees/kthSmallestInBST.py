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

#### Let's try to do it without storing intermediate results in an array ######


def kthSmallestHelper(root, k, i):
    if not root:
        return -math.inf, i

    val, leftI = kthSmallestHelper(root.left, k, i)
    if val != -math.inf:
        return val, i

    i += 1

    if i == k:
        return root.val, i

    return kthSmallestHelper(root.right, k, i)


def kthSmallestConstantSpace(root, k):
    return kthSmallestHelper(root, k, 0)[0]
