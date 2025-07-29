target = 11
nums = [1,1,1,1,1,1,1,1]

def find(nums,target):
    left = 0
    right = 0

    min_length = float('inf')
    arr_sum = nums[left]


    while left <= right and right < len(nums): 
        if arr_sum < target:
            if right == len(nums)-1:
                break
            right += 1
            arr_sum += nums[right]

        elif arr_sum >= target:
            min_length = min(min_length,(right+1)-left)
            arr_sum -= nums[left]
            left += 1


    if min_length > len(nums):
        return 0
    return min_length

print(find(nums,target))