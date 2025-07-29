class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



list1 = ListNode(1)
a = ListNode(2)
b = ListNode(4)

list1.next = a
a.next = b



list2 = ListNode(1)
A = ListNode(3)
B = ListNode(4)

list2.next = A
A.next = B

def dispaly(h):
    curr = h
    element  = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    return ["->".join(element)]


print(dispaly(list1))
print(dispaly(list2))

def mergeTwoLists(list1, list2):
    """
    :type list11: Optional[ListNode]
    :type list22: Optional[ListNode]
    :rtype: Optional[ListNode]
    """
    
    dummy = ListNode(val=-1)
    curr = dummy

    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            curr = list1
            list1 = list1.next
        else:
            curr.next = list2
            curr = list2
            list2 = list2.next

        # if list1 is None and list2 is not None:
        #     curr.next = list2
        #     return dummy.next
        # elif list2 is None and list1 is not None:
        #     curr.next = list1
        #     return dummy.next
    curr.next = list1 if list1 else list2 #this line does the above commented code in one line 
    return dummy.next

h1 = mergeTwoLists(list1,list2)

def dispaly(h1):
    while h1:
        print(h1.val)
        h1 = h1.next

dispaly(h1)