nums = [4, 1, 2, 5, 3, 0]


def bubbleSort(nums):  # O(n^2)
    n = len(nums)  # length of array to be sorted

    is_swapped = False
    for i in range(n-1):

        for j in range(n-1-i):

            if nums[j] > nums[j+1]:
                # flip nums[j] and nums[j+1]
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
                is_swapped = True

        if not is_swapped:
            break


bubbleSort(nums)

print(nums)
