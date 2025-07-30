s = ""



def findMax(s):
    seenHashSet = set()
    max_len = float('-inf')
    i = 0
    j = 0
    while j  < len(s) and i < len(s):
        if s[j] in seenHashSet:
            seenHashSet.clear()
            i += 1
            j = i
            continue
        seenHashSet.add(s[j])
        max_len = max(max_len,len(seenHashSet))
        j += 1
    if max_len <= 0 :
        return 0
    return max_len

print(findMax(s))