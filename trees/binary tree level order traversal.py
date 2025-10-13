from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    ans = []
    q = deque()
    q.append(root)
    ans.append([root.val])
    while q:
        temp = []
        for _ in range(len(q)):
            node = q.popleft()

            if node.left:
                q.append(node.left)
                temp.append(node.left.val)
            if node.right:
                q.append(node.right)
                temp.append(node.right.val)

        if len(temp) > 0:
            ans.append(temp)
    return ans


print(levelOrder(root))
