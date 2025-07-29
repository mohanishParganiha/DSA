nums = [2,7,11,15]
target = 9

class Solution:
    def twoSum(self,nums,target):

        hashset = dict()

        for i in range(len(nums)):

            new_target = target - nums[i]

            if new_target in hashset:
                return [hashset[new_target],i]
            
            hashset[nums[i]] = i

        return 0
    
sol = Solution()
print(sol.twoSum(nums,target))
