from collections import deque
from typing import Optional


class TreeNodes:
    def __init__(self, val: int, left_child=None, right_child=None):
        self.val = val
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return str(self.val)


A = TreeNodes(1)
B = TreeNodes(2)
C = TreeNodes(3)
D = TreeNodes(4)
E = TreeNodes(5)
F = TreeNodes(10)

A.left_child = B
A.right_child = C
B.left_child = D
B.right_child = E
C.left_child = F


# print(A)


def pre_order(node: TreeNodes):
    if not node:
        return

    print(node)
    pre_order(node.left_child)
    pre_order(node.right_child)


# pre_order(A)


def in_order(node: TreeNodes):
    if not node:
        return

    in_order(node.left_child)
    print(node)
    in_order(node.right_child)


# in_order(A)

def post_order(node: TreeNodes):
    if not node:
        return

    post_order(node.left_child)
    post_order(node.right_child)
    print(node)


# post_order(A)


def level_order(nodes: TreeNodes):
    q = deque()
    q.append(nodes)

    while q:
        node = q.popleft()
        print(node)
        if node.left_child:
            q.append(node.left_child)
        if node.right_child:
            q.append(node.right_child)


# level_order(A)


def search(node, target):  # O(n)
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left_child, target) or search(node.right_child, target)


# print(search(A, -1))
# print(search(A, 10))
# print(search(A, 5))


A2 = TreeNodes(5)
B2 = TreeNodes(1)
C2 = TreeNodes(8)
D2 = TreeNodes(-1)
E2 = TreeNodes(3)
F2 = TreeNodes(7)
G2 = TreeNodes(9)

A2.left_child, A2.right_child = B2, C2
B2.left_child, B2.right_child = D2, E2
C2.left_child, C2.right_child = F2, G2

# in_order(A2)


def binary_search_tree_search(node, target):
    if not node:
        return False

    if node.val == target:
        return True

    if target < node.val:
        return binary_search_tree_search(node.left_child, target)
    else:
        return binary_search_tree_search(node.right_child, target)


print(binary_search_tree_search(A2, 5))
