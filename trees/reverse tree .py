from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


A = TreeNode(4)
B = TreeNode(2)
C = TreeNode(7)
D = TreeNode(1)
E = TreeNode(3)
F = TreeNode(6)
G = TreeNode(9)

A.left, A.right = B, C
B.left, B.right = D, E
C.left, C.right = F, G


def invertTree(root: TreeNode) -> TreeNode:

    def in_order(node):
        if not node:
            return
        left = invertTree(node.left)
        right = invertTree(node.right)
        temp = left
        node.left = right
        node.right = left

    in_order(root)
    return root


def level(root: TreeNode) -> None:
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        print(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)


inverted_tree_root = invertTree(A)
level(inverted_tree_root)
