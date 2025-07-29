#variables are dynamicaly typed 
n = 0
print(n,type(n))

n = 'a'
print(n,type(n))

#increment
n = 0
print(n)
n  += 1
print(n)

#None is null
n = 0
print(n,type(n))

n = None
print(n,type(n))

#if and else
n = 1
if n>2:
    print(n)
else :
    print("n is not 2")

# "and"  and "or"
n,m = 1,2
if n == 1 and m == 2:
    print(n,m,"this is true")

n,m = 1,3
if n ==1 or m ==2:
    print("this is true")

#while loop
n = 1
while n < 5:
    print(n)
    n += 1

#for loop
for i in range(5):
    print(i)

for i in range(2,6):
    print(i)

for i in range(5,1,-1):
    print(i)


list_1 = ['a','b',"c",'d']
for i in list_1:
    print(i)

#Division by decimal by default 
print(4/2)

#Divison rounds down
print(4//2)

#mods 
print(10%3)#ans is 1 , returns remaineder

#modding -ve number resultes in errors , import math library to import math.fmod(-10,3) 

#math helper funtions 
import math
math.floor(3/2)
math.ceil(3/2)
math.sqrt(4)
math.pow(2,5)#2 to the power 5

#maximum int 
max_int = float("inf")
#minimum int
min_int = float("-inf")

#array are called lists 
array = [1,2,3]
    #arrays can be used as stack cause they are dynamic 
array.append(4)
array.pop()

    #initaillize the array
arr = [1] * 4 #array with size of 4

    # indexing array with -ve gives item form last so -1 , -2 are last and second last 
    #respectively 

    #slicing 
arr = [1,2,3,4,5]
arr_2 = arr[1:3]

    #enumerate
for i, n in enumerate(list_1):
    print(i,n)#i is index and n is item

    # list comprehension
arr = [i for i in range(5)]

#queue
from collections import deque
que = deque()
que.append(1)
que.append(2)
que.append(3)
que.append(4)

que.pop()#bydefault from end

que.popleft()#pop from start 


#hashset  we can serch and insert value in constant time 

mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet)

    #check if the value exist in has set
print(2 in mySet)

mySet.remove(2)

    #initiallize the hashset
mySet = {i for i in range(4)}


#hastMaps most used also known as dictionary
myMap = {}
myMap["alice"] = 77
myMap["bob"] = 33
print(myMap)

    #length gives number of keys in hash Map
print(len(myMap))

    #serch in hashMap
print("alice" in myMap)

    #pop form hash map
myMap.pop("alice")

    #dictionary comprehension
myMap1 = {i:2*i for i in range(3)}
print(myMap1)

    #looping through map
for key in myMap1:
    print(key,myMap1[key])

for val in myMap1.values():
    print(val)

for key,val  in myMap1.items():
    print(key,val)

#tuples are immutable and are used as keys for hashMaps
tup = (1,2,3)

#heaps
import heapq
    #under the hood the heaps are arrays
minHeap = []
heapq.heappush(minHeap,222)
heapq.heappush(minHeap,3)
heapq.heappush(minHeap,54)
print(minHeap)

heapq.heappop(minHeap)
print(minHeap)

    #build heap form list

arr = [76,2,3,5,3,6]
heapq.heapify(arr)
print(arr)

#functions 
def myfunction(n,m):
    return n*m

#nested functions

def outer(arr,val):
    def helper():
        for i,n in enumerate(arr):
            arr[i] += 2
        #if i use " val += 2" it will only increase the value of val inside of function scope
        #not original
        # you can modify original arrays inside of nested functions but not original values to 
        #work around this we can use "nonlocal" keyword 

        nonlocal val
        val += 2

    helper()
    print(arr,val)

arr = [1,2,3]
val = 3
outer(arr,val)

#classes 
class myClass:

    #constructor 
    def __init__(self,nums:list):
        self.nums = nums
        self.size = len(nums)

    #self keyword
    def getLength(self):
        return  self.size
    
    def getDoubleLenght(self):
        return 2 * self.getLength()
    

a = myClass([1,2,3])
print(a.getLength())
print(a.getDoubleLenght())


