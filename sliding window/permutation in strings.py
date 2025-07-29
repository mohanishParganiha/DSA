from collections import Counter

s1 = "ab"
s2 = "eidbaooo"

def ifPermutationInStrings(s1,s2):
    s1_count = Counter(s1).items()

    left = 0
    right = left + len(s1)-1   # left is at the beginning of window while right at the end , the lenght is equal to length of s1

    while right < len(s2):
        s2_count = Counter(s2[left:right+1]).items()
        if s2_count == s1_count:
            return True
        
        left += 1
        right += 1

    return False


print(ifPermutationInStrings(s1,s2))