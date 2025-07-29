class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

headA = ListNode(4)
a = ListNode(1)
b = ListNode(8)
c = ListNode(4)
d = ListNode(5)

headA.next = a
a.next = b
b.next = c
c.next = d


headB = ListNode(5)
A = ListNode(6)
B = ListNode(1)
C = ListNode(8)
D = ListNode(4)
E = ListNode(5)

headB.next = A
A.next = B
B.next = C
C.next = D
D.next = E


def dispaly(h):
    curr = h
    element  = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    return ["->".join(element)]


print(dispaly(headA))
print(dispaly(headB))


def getIntersectionNode(headA, headB):

    Top = headA
    while Top:
        Bottom = headB
        while Bottom:
            x = Top.val
            y = Bottom.val
            if Top.val == Bottom.val:
                X = Top.next.val
                Y = Bottom.next.val
                if Top.next.val == Bottom.next.val:
                    return Top.val
                
            Bottom = Bottom.next
        Top = Top.next

    return None

print(getIntersectionNode(headA,headB))