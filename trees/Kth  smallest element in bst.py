from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(5)
B = TreeNode(3)
C = TreeNode(6)
D = TreeNode(2)
E = TreeNode(4)
F = TreeNode(1)


A.left, A.right = B, C
B.left, B.right = D, E
D.left = F


def kthSmallest(root: Optional[TreeNode], k: int) -> int:

    def dfs(node: Optional[TreeNode]) -> int:
        nonlocal k

        if not node:
            return None

        lst = dfs(node.left)
        if lst is not None:
            return lst

        k -= 1
        if k == 0:
            return node.val

        rst = dfs(node.right)
        if rst is not None:
            return rst

    return dfs(root)


print(kthSmallest(A, 3))
