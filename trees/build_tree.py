from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(li=None) -> Optional[TreeNode]:
    """building tree from preorder list"""

    if not li:
        return None

    q = deque(li)
    parent_q = deque()
    root = TreeNode(q.popleft())
    parent_q.append(root)
    curr = None

    while q:
        curr = parent_q.popleft()
        child_left = q.popleft()
        child_right = q.popleft()

        if curr:
            if child_left is not None:
                curr.left = TreeNode(child_left)
            if child_right is not None:
                curr.right = TreeNode(child_right)

        if curr.left is not None:
            parent_q.append(curr.left)
        if curr.right is not None:
            parent_q.append(curr.right)

    return root
