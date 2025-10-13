from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)

A.left, A.right = B, C
B.left, B.right = D, E

"""this is one way to do this , find the height of the tree on left and right of each root,
then add them and get max of (lh+rh) and left_subTree_diameter and right_subTree_diameter
"""
# def findHeight(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0
#     return 1 + max(findHeight(root.left), findHeight(root.right))


# def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0
#     lh = findHeight(root.left)
#     rh = findHeight(root.right)
#     main = lh + rh
#     left_diameter = diameterOfBinaryTree(root.left)
#     right_diameter = diameterOfBinaryTree(root.right)

#     return max(main, left_diameter, right_diameter)

"""another way of doing this is to use main variable in height functions and it will
set main = max(main,(lh+rh))"""


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    diameter = [0]

    def findHeight(node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        lh = findHeight(node.left)
        rh = findHeight(node.right)
        diameter[0] = max(diameter[0], (lh+rh))
        return 1 + max(lh, rh)

    findHeight(root)
    return diameter[0]


print(diameterOfBinaryTree(A))
