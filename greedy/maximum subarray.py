def maxSubArray(nums: list[int]) -> int:  # type: ignore
    max_sum = float('-inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))


def maxSubArray(nums: list[int]) -> int:
    max_sum = float('-inf')
    curr_sum = 0
    j = 0
    while j < len(nums):
        curr_sum += nums[j]
        max_sum = max(max_sum, curr_sum)
        if curr_sum < 0:
            curr_sum = 0
            j += 1
            continue
        j += 1
    return max_sum


nums = [-4, -3]
print(maxSubArray(nums))
