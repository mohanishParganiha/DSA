from collections import Counter
nums = [1,1,1,2,2,3]
strs = ['a','a','a','b','b','c']
k = 2

class Solution(object):
    def topKFrequent(self, nums, k):

        list_a = []
        countr = Counter(nums).most_common(k)
        for i in countr:
            list_a.append(i[0])

        return list_a
    
sol = Solution()
print(sol.topKFrequent(nums,k))