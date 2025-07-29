from collections import Counter

s = "badc"
t = "baba"


def isIsomorphic(s,t):
    hashMap = dict()
    for i in range(len(s)):
        if  s[i] in hashMap and hashMap[s[i]] != t[i]:
                return False
        elif t[i] in hashMap.values() and s[i] not in hashMap:
                return False
        hashMap[s[i]] = t[i]
    return True
print(isIsomorphic(s,t))

