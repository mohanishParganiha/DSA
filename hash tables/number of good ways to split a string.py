from collections import defaultdict

s = "aacaba"

left = dict()
right = dict()

for index, char in enumerate(s):
    if char not in left:
        left[char] = index
    right[char] = index

indexs = list(left.values()) + list(right.values())
indexs = sorted(indexs)

mid = len(indexs)//2

print(indexs[mid]-indexs[mid-1])

