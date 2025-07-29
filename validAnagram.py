from collections import Counter

s = "rat"
t = "car"

class Solution:
    def isAnagram(self,s,t):
        if not len(s) == len(t):
            return False
        dict_s = dict(Counter(s))
        dict_t = dict(Counter(t))

        for i in dict_s:
            if not i in dict_t:
                return False
            if not dict_s[i] == dict_t[i]:
                return False

        else:
            return True



sol = Solution()
print(sol.isAnagram(s,t))