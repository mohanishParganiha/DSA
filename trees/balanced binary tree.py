from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(2)
D = TreeNode(3)
E = TreeNode(3)
F = TreeNode(4)
G = TreeNode(4)

A.left, A.right = B, C
B.left, C.right = D, E
D.left, E.right = F, G


def isBalanced(root: Optional[TreeNode]) -> bool:
    if not root:
        return True

    def findHeight(node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        lh = findHeight(node.left)
        if lh == -1:
            return -1

        rh = findHeight(node.right)
        if rh == -1:
            return -1

        if abs(lh-rh) > 1:
            return -1

        return 1 + max(lh, rh)

    return findHeight(root) != -1


print(isBalanced(A))
