nums = [5, 1, 3]
target = 5


def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        # check if the nums[mid] is greater than nums[left] then its in left part

        if nums[left] <= nums[mid]:

            # check if the target lies between left and mid if so then move right
            if nums[left] <= target < nums[mid]:
                right = mid - 1

            # if not then move left
            else:
                left = mid + 1

        else:
            # check if the target is between right and mid if so then move left
            if nums[mid] < target <= nums[right]:
                left = mid + 1

            # if not then move right
            else:
                right = mid - 1

    return -1


print(search(nums, target))
