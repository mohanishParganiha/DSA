from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


root = TreeNode(3)
A = TreeNode(4)
B = TreeNode(5)
C = TreeNode(1)
D = TreeNode(2)

root.left, root.right = A, B
A.left, A.right = C, D

subRoot = TreeNode(4)
a = TreeNode(1)
b = TreeNode(2)

subRoot.left, subRoot.right = a, b


def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

    def sameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return sameTree(p.left, q.left) and sameTree(p.right, q.right)

    def dfs_traverse(node: Optional[TreeNode]) -> bool:
        if not node:
            return False

        if node.val == subRoot.val:
            if sameTree(node, subRoot):
                return True

        return dfs_traverse(node.left) or dfs_traverse(node.right)

    return dfs_traverse(root)


print(isSubtree(root, subRoot))
