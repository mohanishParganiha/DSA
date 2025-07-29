nums = [1,2,3,4,5,6,7]
k = 6
res = [None] * len(nums)

for i in range(len(nums)):
    if i+k < len(nums):
        res[i+k] = nums[i]
    else:
        res[i-k-1]= nums[i]
nums = res.copy()
print(nums)