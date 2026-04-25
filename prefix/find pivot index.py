def pivotIndex(nums: list[int]) -> int:
    if not nums:
        return -1
    if len(nums) == 1:
        return 0

    prev = 0
    prefix_sum = [0]*len(nums)
    for i in range(len(nums)):
        prefix_sum[i] = nums[i]+prev
        prev += nums[i]
    print(prefix_sum)

    prev = 0
    suffix_sum = [0]*len(nums)
    for i in range(len(nums)-1, -1, -1):
        suffix_sum[i] = nums[i]+prev
        prev += nums[i]

    print(suffix_sum)

    for i in range(len(nums)):
        if i == 0:
            if suffix_sum[i+1] == 0:
                return i
        elif i == len(nums)-1:
            if prefix_sum[i-1] == 0:
                return i
        else:
            if prefix_sum[i-1] == suffix_sum[i+1]:
                return i

    return -1


list1 = [1, 7, 3, 6, 5, 6]
print(pivotIndex(list1))
