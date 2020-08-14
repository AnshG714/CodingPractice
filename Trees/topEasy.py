from Tree import *


def mergeTrees(root1, root2):
    """
    Given two binary trees and imagine that when you put one of them to cover the 
    other, some nodes of the two trees are overlapped while the others are not.

    You need to merge them into a new binary tree. The merge rule is that if two 
    nodes overlap, then sum node values up as the new value of the merged node. 
    Otherwise, the NOT null node will be used as the node of new tree.

      Input: 
      Tree 1                     Tree 2                  
             1                         2                             
            / \                       / \                            
           3   2                     1   3                        
          /                           \   \                      
          5                             4   7                  
    Output: 
    Merged tree:
           3
          / \ 
         4   5
        / \   \ 
       5   4   7
    """

    if not root1 and not root2:
        return None
    elif not root2:
        return root1
    elif not root1:
        return root2
    else:
        newNode = TreeNode(root1.val + root2.val)
        newNode.left = mergeTrees(root1.left, root2.left)
        newNode.right = mergeTrees(root1.right, root2.right)

        return newNode


def maxDepth(root: TreeNode):
    """
    Given a binary tree, find its maximum depth.

    The maximum depth is the number of nodes along the longest path from the root 
    node down to the farthest leaf node.
    Note: A leaf is a node with no children.
    """
    if not root:
        return 0

    return 1 + max(maxDepth(root.left), maxDepth(root.right))


def invertTree(root):
    """
    Invert a binary tree
    """

    if not root:
        return root

    leftInv = invertTree(root.left)
    rightInv = invertTree(root.right)

    root.left = rightInv
    root.right = leftInv

    return root


def diameterOfTree(root):
    """
    Given a binary tree, you need to compute the length of the diameter of the 
    tree. The diameter of a binary tree is the length of the longest path between 
    any two nodes in a tree. This path may or may not pass through the root.
    """

    if not root:
        return 0

    hl = maxDepth(root.left)
    hr = maxDepth(root.right)

    dl = diameterOfTree(root.left)
    dr = diameterOfTree(root.right)

    return max(hl + hr, max(dl, dr))


def isMirror(root1, root2):
    """
    Decide whether the binary trees with roots root1 and root2 are mirrors of
    each other
    """
    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False

    return root1.val == root2.val and isMirror(root1.left, root2.right) \
        and isMirror(root1.right, root2.left)


def isSymmetric(root):
    return isMirror(root, root)


def trimBST(root, L, R):
    """
    Given a binary search tree and the lowest and highest boundaries as L and R, 
    trim the tree so that all its elements lies in [L, R] (R >= L). You might 
    need to change the root of the tree, so the result should return the new 
    root of the trimmed binary search tree.
    """
    if L <= root.val <= R:
        root.left = trimBST(root.left, L, R)
        root.right = trimBST(root.right, L, R)
        return root
    elif root.val < L:
        return trimBST(root.right, L, R)
    else:
        return trimBST(root.left, L, R)
