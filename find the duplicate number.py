nums = [1, 3, 4, 2, 2]


def findDuplicated(nums: list[int]) -> int:
    nums.sort()

    prev = -1
    for num in nums:
        if num != prev:
            prev = num
        else:
            return num


print(findDuplicated(nums))
