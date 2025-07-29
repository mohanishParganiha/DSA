nums = [1,5,4,2,9,9,9]
k = 3
from collections import defaultdict


def findMaxSum(nums,k):
    max_sum = 0
    temp = 0

    seen_counter = defaultdict(int)

    left = 0
    right = 0

    while right < len(nums):
        if right - left <= k-1:
            seen_counter[nums[right]] += 1
            temp += nums[right]
            right += 1
            
        else:
            temp += nums[right]
            seen_counter[nums[right]] += 1
            temp -=  nums[left]
            seen_counter[nums[left]] -= 1

            if seen_counter[nums[right]] <= 0:
                seen_counter.pop(nums[right])
            elif seen_counter[nums[left]] <= 0:
                seen_counter.pop(nums[left])

            left += 1
            right += 1


        
        if len(seen_counter) == k:
            max_sum = max(max_sum,temp)




    return max_sum

print(findMaxSum(nums,k))