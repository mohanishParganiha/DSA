from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(5)
B = TreeNode(4)
C = TreeNode(6)
D = TreeNode(3)
E = TreeNode(7)

A.left, A.right = B, C
C.left, C.right = D, E


def isValidBST(root: Optional[TreeNode]) -> bool:

    def dfs_traverse(node: Optional[TreeNode], low: float, high: float) -> bool:
        if not node:
            return True

        if not (low < node.val < high):
            return False

        lst = dfs_traverse(node.left, low, node.val)
        if not lst:
            return False

        rst = dfs_traverse(node.right, node.val, high)
        if not rst:
            return False

        return True

    return dfs_traverse(root, float('-inf'), float('inf'))


print(isValidBST(A))
