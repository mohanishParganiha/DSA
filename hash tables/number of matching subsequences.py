from collections import Counter
s = "abcde"
words = ["a","bb","acd","ace"]


def bs(idx_list:list,index:int):
    L = 0
    R = len(idx_list)

    while L < R:
        mid = L+R//2
        if index < idx_list[mid]:
            R = mid
        else:
            L = mid + 1
        
    return L

hashmap = dict()
for i, c in enumerate(s):
    if c not in hashmap:
        hashmap[c] = []
    hashmap[c].append(i)

out = 0

for word in words:
    found = True
    index = -1
    for char in word:
        if char not in hashmap:
            found = False
            break
        idx_list = hashmap[char]
        pos = bs(idx_list,index)

        if pos==len(idx_list) : 
            found = False
            break
        index = idx_list[pos]
    if found:
        out += 1

print(out)