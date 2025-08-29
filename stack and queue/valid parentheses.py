# one way to do this , this break when the string lenght is 1 or 0 ,
# and if string starts with closing braket

"""s = ")"
stack = []
for char in s:
    if char == ')':
        if stack[-1] == '(':
            stack.pop()
            continue
    elif char == ']':
        if stack[-1] == '[':
            stack.pop()
            continue
    elif char == '}':
        if stack[-1] == '{':
            stack.pop()
            continue

    stack.append(char)

if len(stack) > 0:
    print(False)
else:
    print(True)
"""

# another way is to append before anything else and then check for pairs , if found remove them both

# this is way to complex for this simple question , to check if there is a pair

"""s = "()"
stack = []
for char in s:
    stack.append(char)
    if len(stack) <= 1:
        continue
    if char == ')':
        if stack[-2] == '(':
            stack.pop()
            stack.pop()
            continue
    elif char == ']':
        if stack[-2] == '[':
            stack.pop()
            stack.pop()
            continue
    elif char == '}':
        if stack[-2] == '{':
            stack.pop()
            stack.pop()
            continue"""


# to check if we have a pair we can creat a hashmap and put the close as key , and open as value
# we can check if the stack[-1] matches the value of hash_map[char] , if then pop them

s = "()"

hash_map = {'}': '{', ')': '(', ']': '['}
stack = []

for char in s:
    if stack and hash_map[char] == stack[-1]:
        stack.pop()
        continue
    stack.append(char)


if len(stack) > 0:
    print(False)
else:
    print(True)
