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

head.next = a
a.next = b
b.next = c


def reorderList(head: Optional[ListNode]) -> None:
    """
    Do not return anything, modify head in-place instead.
    """

    # step1 find middle point ,we can use
    #   slow ,fast pointers ,1step fo slow is 2step
    #   of fast ,
    slow = head
    fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    # step 2 ,reverse the second half of list
    second = slow.next
    slow.next = None
    node = None

    while second:
        temp = second.next
        second.next = node
        node = second
        second = temp

    # step 3, join the 2 list in alternate order
    first = head
    second = node
    while head and second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2


display(head)
reorderList(head)
display(head)
