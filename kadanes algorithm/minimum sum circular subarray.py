nums  = [5,-3,5]

def maxSubarraySum(nums):
    max_sum = float('-inf')
    curr_max_sum = 0

    for i in range(len(nums)):
        if curr_max_sum + nums[i] >= max_sum:
            curr_max_sum += nums[i]
            max_sum =curr_max_sum

    return max_sum
-=S
print(maxSubarraySum(nums))