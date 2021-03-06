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


def kthSmallestHelper(root, nums, k):
    if not root:
        return

    kthSmallestHelper(root.left, nums, k)
    nums[0] += 1

    if nums[0] == k:
        nums[1] = root.val
        return

    kthSmallestHelper(root.right, nums, k)


def kthSmallestConstantSpace(root, k):
    nums = [0, 0]
    kthSmallestHelper(root, nums, k)
    return nums[1]
