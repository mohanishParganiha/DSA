from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(2)
B = TreeNode(4)
C = TreeNode(10)
D = TreeNode(8)
E = TreeNode(4)

A.right = B
B.left, B.right = C, D
D.right = E


def goodNodes(root: TreeNode) -> int:
    if not root:
        return
    good_nodes = [1]

    def dfs_traversal(node: TreeNode, max_node: int):
        if not node:
            return

        if node.val >= max_node:
            good_nodes[0] += 1

        max_node = max(max_node, node.val)

        dfs_traversal(node.left, max_node)
        dfs_traversal(node.right, max_node)

    dfs_traversal(root.left, root.val)
    dfs_traversal(root.right, root.val)
    return good_nodes[0]


print(goodNodes(A))
