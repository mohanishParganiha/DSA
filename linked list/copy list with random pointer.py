from typing import Optional


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        return str(self.val)


def display(head: Optional[Node]):
    curr = head
    while curr:
        print("val,next,random", str([curr.val, str(curr.next), curr.random]))
        curr = curr.next


head = Node(val=1)
a = Node(val=2)
b = Node(val=3)
c = Node(val=4)
d = Node(val=5)

head.next = a
a.next = b
b.next = c
c.next = d


display(head)


def deepCopy(head: Optional[Node]) -> Optional[Node]:
    """first pass we create a deep duplicate of list , with its next values """
    curr1 = head
    hash_map = {}
    while curr1:
        if curr1 not in hash_map:
            hash_map[curr1] = Node(val=curr1.val)

        curr1 = curr1.next

    """second pass we will create join each nodes in new list and join random pointer
    to do that we will use hashmap which has original nodes mapped to new nodes ,
    we traverse through original list and each node we check hashmap and map new nodes on new list"""

    curr = head
    while curr:
        if curr.next is None:
            hash_map[curr].next = None
        else:
            hash_map[curr].next = hash_map[curr.next]
        if curr.random is None:
            hash_map[curr].random = None
        else:
            hash_map[curr].random = hash_map[curr.random]

        curr = curr.next

    return hash_map[head]


deep_copy_lis = deepCopy(head)
display(deep_copy_lis)
