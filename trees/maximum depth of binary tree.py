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
B.left = D
C.right = E

# # using level order traversal to process


# def maxDepth(root: Optional[TreeNode]) -> int:
#     depth = 0
#     if not root:
#         return 0
#     q = deque()
#     q.append(root)
#     """normal level_order_traversal wont work , it process all the child in single loop as we pop from left
#         to fix this we need to process all child in a level in another loop ,,
#     """
#     while q:
#         for _ in range(len(q)):
#             node = q.popleft()
#             if node.left:
#                 q.append(node.left)

#             if node.right:
#                 q.append(node.right)

#         depth += 1

#     return depth


# print(maxDepth(A))


# using dfs with recursion


def maxDepth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


print(maxDepth(A))
