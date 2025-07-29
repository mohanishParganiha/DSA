nums = [1,2,3,1]

class Solution:
    def containsDuplicate(self,nums):

        unique = set(nums) #build a new set with nums to remove duplicates 
        if len(nums) == len(unique): #to check  if the lenght of original and new are same 
            return False    # if same then original contains no duplicate then return false
        else:
            return True # if not same then original contains duplicate return true
        
sol = Solution()
print(sol.containsDuplicate(nums))