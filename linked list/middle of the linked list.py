class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
a = ListNode(2)
b = ListNode(3)
c = ListNode(4)
d = ListNode(5)

head.next = a
a.next = b
b.next = c
c.next = d

Fast = Slow = head

while Fast and Slow:
    if Fast.next is None:
        break
    Slow = Slow.next
    Fast = Fast.next.next
print(Slow.val)