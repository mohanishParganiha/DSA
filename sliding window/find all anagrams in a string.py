from collections import Counter


def isAnagram(s,p_count):
    s_count = Counter(s)

    return (s_count == p_count)  
        


s = "cbaebabacd"
p = "abc"

window_length = len(p)-1
p_count = Counter(p)
left = 0
right = left + window_length
ans = []

while right < len(s):
    if right-left < len(p):
        if  isAnagram(s[left:right+1],p_count):
            ans.append(left)
    left += 1
    right = left + window_length

print(ans)