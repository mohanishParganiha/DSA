from collections import deque


class Stack:
    def __init__(self) -> None:
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self) -> int:
        length = len(self.q1)
        for _ in range(length-1):
            self.q2.append(self.q1.popleft())
        item = self.q1.popleft()
        temp = self.q1
        self.q1, self.q2 = self.q2, temp
        return item

    def top(self) -> int:
        length = len(self.q1)
        for _ in range(length-1):
            self.q2.append(self.q1.popleft())
        item = self.q1.popleft()
        self.q2.append(item)
        temp = self.q1
        self.q1, self.q2 = self.q2, temp
        return item

    def empty(self) -> bool:
        return len(self.q1) == 0


mystack = Stack()
mystack.push(1)
mystack.push(2)
print(mystack.top())
print(mystack.pop())
print(mystack.empty())
