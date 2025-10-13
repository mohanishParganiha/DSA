from typing import Optional


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


head1 = ListNode(2)
a = ListNode(4)
b = ListNode(3)


head1.next = a
a.next = b

head2 = ListNode(5)
a2 = ListNode(6)
b2 = ListNode(4)

head2.next = a2
a2.next = b2


def display(head: Optional[ListNode]) -> None:
    curr = head
    while curr:
        print(curr.val)

        curr = curr.next


"""
1 way to solve .

-iterate through both list and convert them into number.
-add them
-put them into list reversed

"""


def addTwoNumbers(head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:

    num1 = 0
    place = 1
    curr = head1
    while curr:

        num1 = curr.val*place + num1

        curr = curr.next
        place *= 10

    num2 = 0
    place = 1
    curr = head2
    while curr:

        num2 = curr.val*place + num2

        curr = curr.next
        place *= 10

    nums = num1 + num2

    new_list = ListNode(val=nums % 10)

    nums = nums // 10

    curr = new_list

    while nums > 0:

        digit = nums % 10

        curr.next = ListNode(val=digit)

        curr = curr.next

        nums = nums // 10

    return new_list


display(addTwoNumbers(head1, head2))


"""second way to do it """
