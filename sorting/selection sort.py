nums = [4, 1, 5, 2, 3]


def selectionSort(nums):  # O(n^2)
    n = len(nums)

    for i in range(n):  # O(n)
        smallest = i  # assign the index of smallest items , lets asssume its the first one

        for j in range(i+1, n):  # the range is from i+1 -> n-1     O(n)
            if nums[j] <= nums[smallest]:
                smallest = j

        temp = nums[i]
        nums[i] = nums[smallest]
        nums[smallest] = temp


selectionSort(nums)
print(nums)
