class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


head = ListNode(1)
a = ListNode(1)
b = ListNode(2)
# c = ListNode(3)
# d = ListNode(3)

head.next = a
a.next = b
# b.next = c
# c.next = d

def deleteDuplicates( head):
    curr = head
    prev = ListNode(-1)
    return1 = prev
   
    while prev and curr: 
        if not prev.val == curr.val:
            prev.next = curr
            prev = prev.next
        
        

        curr = curr.next



    return return1


h1 = deleteDuplicates(head)

while h1:
    print(h1.val)
    h1 = h1.next
