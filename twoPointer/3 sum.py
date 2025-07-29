import collections

nums = [-1,0,1,2,-1,-4]
target = 0

def threeSum(nums:list,target:int):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if i > 0 and nums[i-1] == nums[i]:
                continue
        new_target = nums[i]
        L = i+1
        R = len(nums)-1
        while L < R:
            if nums[L] + nums[R] + new_target < 0:
                L += 1
            elif nums[R] + nums[L] + new_target > 0:
                R -= 1
            else:
                ans.append([nums[L],nums[R],new_target])
                L += 1
                while L < R and nums[L] == nums[L-1]:
                    L += 1

    return ans

print(threeSum(nums,target))