# to implement a stack we can you dynamic arrays or linked list 

#most of the time it is implemented as dynamic arrays 

#functions of stack
#works on princeple of LIFO (last in fist out)  
    # meaning which ever item if put last , it will come out first
# stack operations are : 
    # append() , add to last
    # pop() , remove form last
    #peek , check the top item(last index of array) arr[-1]
    #if empty , check if stack is empty or not 
            #we need to check stack is empty or not cause if poped empty stack it throws error

stack = []

print(stack)

stack.append(1)
print(stack)
stack.append(2)
print(stack)
stack.append(3)
print(stack)

#check last item(top item)
print('last item',stack[-1])

#we store item we poped 
a = stack.pop()
print(a)
a = stack.pop()
print(a)
a = stack.pop()
print(a)


#check if stack is emtpy or not
if stack:
    print(False)
else:
    print(True)


#pop item inside of check 
if stack:
    stack.pop()



#__________________________________________________________________________

# queue are implemented through arrays or linked list 
#mostly it is implemented throught linked list
# we use dequeue form collections 
# queue use FIFO (first in first out) which ever item was put in queue first its out first
# queue also has 
    # append 
    #pop left  /right
    #peek form left / right


from collections import deque

queue = deque()
queue.append(1)
print(queue)
queue.append(2)
print(queue)
queue.append(3)
print(queue)

print('\n')
print('peek from left',queue[0])
print('peek from right',queue[-1])
print('\n')

print(queue)
queue.popleft()
print('popped from left',queue)
queue.pop()
print('poped from right',queue)