from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A0 = TreeNode(1)
B0 = TreeNode(2)

A0.left = B0


A1 = TreeNode(1)
B1 = TreeNode(2)

A1.right = B1


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def checkTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> int:
        if not p and not q:
            return 0
        if not p:
            return -1
        if not q:
            return -1

        left_side = checkTree(p.left, q.left)
        if left_side == -1:
            return -1

        right_side = checkTree(p.right, q.right)
        if right_side == -1:
            return -1

        if p.val != q.val:
            return -1

        return 1
    return checkTree(p, q) != -1


print(isSameTree(A0, A1))
