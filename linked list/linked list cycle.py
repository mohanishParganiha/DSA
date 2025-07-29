from collections import Counter
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(3)
a = ListNode(2)
b = ListNode(0)
c = ListNode(-4)

head.next = a
a.next =b
b.next = c
c.next = a

# this approach works but implementation is wrong revist this problem to under stand this

# def hasCycle( head):
#     """
#     :type head: ListNode
#     :rtype: bool
#     """
    

#     Slow = head
#     Fast = ((head.next).next).next
#     while Slow and Fast:
#         if Slow == Fast: #check if they are same
#             return True #if they are then true
#         else:
#             Slow = Slow.next # if not then increment slow pointer by one 
#             Fast = ((Fast.next).next).next
        
#     return True

# print(hasCycle(head))

def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """

    Slow = head
    Fast = head
    while Fast.next and Fast:
        Slow = Slow.next 
        Fast = (Fast.next).next

        if Slow == Fast: 
            return True 
        
    return False