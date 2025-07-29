# in python we implement linked list as classes
#in linked list we have head(start) and pointers(which points at next values through address)

# to add node in btween , we have to start from head to that index , then adjust the pointers 
# ->1-> 2->4->
# ->1-> 2-> 3 -> 4->
#we added 3 in btwn and adjust the pointers 

#adding in linked list is O(n) and looking up is also O(n)
#removing is also O(n)
#adding at start is O(1)

#we most of the time use doubly linked list 
# in this the pointer not only point to next value but also last value 


#singly linked list 

class SinglyLinked:
    def __init__(self,val,next = None):
        self.val = val
        self.next  = next
    
    def __str__(self):
        return str(self.val)
    
#making singly linked list

head = SinglyLinked(1)
a = SinglyLinked(3)
b = SinglyLinked(4)

head.next = a
a.next = b

print(head)

#traversing singly linked list
curr = head

while curr:
    print(curr)
    curr = curr.next


# display linked list - O(n)
def display(head):
    curr=head
    element = []
    while curr:
        element.append(str(curr.val))
        curr = curr.next
    print("->".join(element))
display(head)


#search a node value -O(n)
def searchNode(head,val):
    curr = head
    while curr:
        if curr.val == val:
            return True
        curr = curr.next
    return False
print(searchNode(head,3))


## doubly linked list

class doublyNode:
    def __init__(self,val,next = None,prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return self.val
    

Head = Tail = doublyNode(1)    # this is head first node


#traversing through doubly linked list 
curr = Head
while curr:
    print(curr.val)
    curr = curr.next

# display 
def doublyDisplay(Head):
    curr= Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print('<->'.join(elements))

#insert at beginning 
def insert_at_beginning(head,tail,val):
    new_node = doublyNode(val,next=head)
    head.prev = new_node
    return new_node,tail #return new node cause new node is not head and tail is tail 

Head,Tail = insert_at_beginning(Head,Tail,3)
doublyDisplay(Head)

#insert at end - O(n)
def insert_at_end(head,tail,val):
    new_node = doublyNode(val,prev=tail)
    tail.next = new_node
    return head,new_node

Head,Tail  = insert_at_end(Head,Tail,4)
doublyDisplay(Head)