nums = [2, 1]


def findMin(nums: list[int]) -> int:

    min_value = float('inf')

    left = 0
    right = len(nums)-1

    while left <= right:
        mid = (left + right) // 2

        min_value = min(min_value, nums[mid])

        if nums[mid] >= nums[left] and nums[left] > nums[right]:
            left = mid + 1

        else:
            right = mid - 1

    return min_value


print(findMin(nums))
