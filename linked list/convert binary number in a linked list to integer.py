# head = [1,0,1]

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = ListNode(1)
a = ListNode(0)
b = ListNode(1)

head.next = a
a.next = b


def convert(head):
    curr = head
    temp = ''
    while curr:
        if curr.val is not None:
            temp += str(curr.val)
        curr = curr.next
    return(int(temp,2))
convert(head)