from Tree import *


def lowestCommonAncestorOfBST(root: TreeNode, p: TreeNode, q: TreeNode):
    if p == root or q == root:
        return root
    elif p.val < root and q.val > root or p.val > root and q.val < root:
        return root
    elif p.val < root:
        return lowestCommonAncestorOfBST(root.left, p, q)
    else:
        return lowestCommonAncestorOfBST(root.right, p, q)
