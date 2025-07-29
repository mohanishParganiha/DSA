
# hash map with arrays 

# class MyHashMap(object):

#     def __init__(self):
#         self.key = []
#         self.value = []
#         self.length = 0

#     def put(self, key, value):
#         """
#         :type key: int
#         :type value: int
#         :rtype: None
#         """
#         self.key.append(key)
#         self.value.append(value)
#         self.length = len(self.key)

#     def get(self, key):
#         """
#         :type key: int
#         :rtype: int
#         """
#         for k in range(self.length):
#             if self.key[k] == key:
#                 return self.value[k]
#         return -1
#     def remove(self, key):
#         """
#         :type key: int
#         :rtype: None
#         """
        
#         for k in range(self.length):
#             if self.key[k] == key:
#                 self.key.pop(k)
#                 self.value.pop(k)
#                 self.length = len(self.key)
#                 return  None
#         return -1
    
#______________________________________________________ hash map with linked list

class ListNode:
    def __init__(self,next = None,value  = None,key = None,):
        self.value = value
        self.next = next
        self.key = key


class MyHashMap(object):

    def __init__(self):
        self.head = ListNode()


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
          
        curr = self.head
        while curr:
            if curr.key == key:
                curr.value = value
                return None
            curr = curr.next

        temp = ListNode(value=value,key=key,next=self.head)
        self.head = temp
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        curr = self.head
        while  curr:
            if curr.key == key:
               return curr.value
            curr = curr.next
        return -1
    
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        curr = self.head
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return None
            prev = curr
            curr = curr.next

myHashMap = MyHashMap()
myHashMap.put(1, 1)
myHashMap.put(2, 2)
print(myHashMap.get(1))  
print(myHashMap.get(3))
myHashMap.put(2, 1)
print(myHashMap.get(2))
myHashMap.remove(2) 
print(myHashMap.get(2))

# myHashMap.put(1,1)
# print(myHashMap.get(1))