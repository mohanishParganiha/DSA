s = "qrsvbspk"



def findMax(s):
    left = right = 0
    seen = dict()

    max_len = 0

    if len(s) == 1:
        return 1
    elif len(s) == 0:
        return 0

    while left < len(s) and right < len(s):
        if s[right] in seen:
            max_len = max(max_len,right-left)
            seen.pop(s[left])
            left += 1
        seen[s[right]] = right
        right += 1


    return max_len


print(findMax(s))