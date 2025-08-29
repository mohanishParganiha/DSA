# 2 ways to doing this , 1st is using DLL (doubly linked list ) little difficult but doable ,
# another way of doing it is uisng 2 stacks(arrays)

class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = [float('inf')]

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        if self.min_stack and val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        last = self.main_stack.pop()
        if self.min_stack[-1] == last:
            self.min_stack.pop()

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
