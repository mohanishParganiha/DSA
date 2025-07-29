nums = [-2,1,-3,4,-1,2,1,-5,4]

def maximumSubarraySum(nums):

    max_sum = float('-inf')
    curr_max_sum = 0

    i = 0
    while i < len(nums):
        curr_max_sum += nums[i]

        if curr_max_sum  >= max_sum:
            max_sum = max(max_sum,curr_max_sum)
    
            
        if curr_max_sum < 0:
            curr_max_sum = 0


        i += 1

    return max_sum

print(maximumSubarraySum(nums))