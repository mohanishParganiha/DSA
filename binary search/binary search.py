nums = [5]
target = 5


def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums)-1

    while left < right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            left = mid+1
        elif target < nums[mid]:
            right = mid-1

    if right == left:
        return -1


print(search(nums, target))
