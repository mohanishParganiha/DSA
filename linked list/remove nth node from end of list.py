from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def display(head: Optional[ListNode]):
    temp_list = []
    curr = head
    while curr:
        temp_list.append(curr.val)
        curr = curr.next
    print(temp_list)


head = ListNode(val=1)
a = ListNode(val=2)
b = ListNode(val=3)
c = ListNode(val=4)
d = ListNode(val=5)

head.next = a
a.next = b
b.next = c
c.next = d

display(head)


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:

    size = 0
    curr = head
    while curr:
        size += 1
        curr = curr.next

    target = size - n

    if target == 0:
        return head.next

    prev = None
    curr = head
    next_node = curr.next
    for i in range(target):
        prev = curr
        curr = curr.next
        next_node = curr.next

    prev.next = next_node

    return head


new_head = removeNthFromEnd(head, 5)
display(new_head)
