from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    hash_map = {k: v for v, k in enumerate(inorder)}
    pre_idx = 0

    def build(lower_bound: int, upper_bound: int):
        nonlocal pre_idx

        if lower_bound > upper_bound:
            return

        root = TreeNode(preorder[pre_idx])
        pre_idx += 1

        index = hash_map[root.val]

        root.left = build(lower_bound, index-1)
        root.right = build(index+1, upper_bound)

        return root

    return build(0, len(preOrder)-1)


preOrder = [3, 9, 20, 15, 7]
inOrder = [9, 3, 15, 20, 7]

obj = buildTree(preorder=preOrder, inorder=inOrder)


def dfs(node):
    if not node:
        return None

    print(node.val)
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)


dfs(obj)
