class ListNode():
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

curr  = head
prev = None
while curr:

    temp = curr.next 
    curr.next = prev
    prev = curr
    curr = temp
 
curr = prev
while curr:
    print(curr.val)
    curr = curr.next