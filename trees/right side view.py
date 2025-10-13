from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(5)
E = TreeNode(4)

A.left, A.right = B, C
B.right = D
C.right = E


def rightSideView(root: Optional[TreeNode]) -> list[int]:
    """we can use level order traversal , and return the last child (right most child on eveyr loop)"""

    ans = []
    q = deque()
    q.append(root)

    while q:
        level_size = len(q)
        for i in range(level_size):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if i == level_size - 1:
                ans.append(node.val)
    return ans


print(rightSideView(A))
