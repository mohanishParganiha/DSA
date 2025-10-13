from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(3)
a = ListNode(5)


head.next = a

left = 1
right = 2


def reverseListInBetweenLeftAndRight(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    prev = dummy

    for _ in range(left-1):
        prev = prev.next

    curr = prev.next
    for _ in range(right-left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp

    return dummy.next


h1 = reverseListInBetweenLeftAndRight(head, left, right)
curr = h1
while curr:
    print(curr.val)
    curr = curr.next
