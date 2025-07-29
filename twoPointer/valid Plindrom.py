s = "A man, a plan, a canal: Panama"


def isPalindrome(s:str):
    n = len(s)
    i,j = 0,n-1

    s = s.lower()

    while i < n and j > 0:
        
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() == s[j].lower():
            i += 1
            j -= 1
            continue
        else:
            return False
        
    return True

print(isPalindrome(s))