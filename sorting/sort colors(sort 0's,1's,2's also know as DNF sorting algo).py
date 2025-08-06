nums = [2, 0, 2, 1, 1, 0]
"""
red  - 0
white - 1
blue - 2

1- brute force , using 2 loops
2- optimized approach , using single loop , count 0's ,1's ,2's and over write the orginal
    array as numbers of 0's,1's,2's,
3 - we take 3 pointer low,mid,high, and we assign different parts of the array shuch as ,
    [0,0,0,1,1,1,...,2,2,2]
    0's is in between 0th index and (low-1) pointer
    1's is in between low and mid-1 pointers
    2's is in between high+1 to  n-1 pointers

    the unsorted part of arary is in between mid to high , so we start with how array as unsorted ,
    low = 0
    mid = 0
    high = n-1

    we move mid towards high

    check if nums[mid] == 0, swap nums[low] with nums[mid], increase low by +1 , mid by +1
    check if nums[mid] == 1,  , increase mid by +1
    check if nums[mid] == 2, swap nums[mid] with nums[high], reduce high by -1

    continue

    """


def sorting(nums):
    count0 = 0
    count1 = 0
    count2 = 0
    """

    #using 2nd approach
    for i in range(len(nums)): # O(n)
        if nums[i] == 0:
            count0 += 1
        elif nums[i] == 1:
            count1 += 1
        else:
            count2 += 1

    for i in range(len(nums)):  # O(n)
        if count0 > 0:
            nums[i] = 0
            count0 -= 1
        elif count1 > 0:
            nums[i] = 1
            count1 -= 1
        elif count2 > 0:
            nums[i] = 2

    # total time complexity is O(2n) -> O(n) , the loop only runs twice
    # space complexity is O(1), only 3 variables are used no arrays

    """

    # using  3rd approach also know as DNF sorting algorithm or danish national flag sorting algo

    low = 0
    mid = 0
    high = len(nums)-1
    count = 0

    while mid <= high:
        count += 1
        if nums[mid] == 0:
            # sawp mid to low , move low += 1, mid +=1
            temp = nums[low]
            nums[low] = nums[mid]
            nums[mid] = temp
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        else:
            temp = nums[high]
            nums[high] = nums[mid]
            nums[mid] = temp
            high -= 1
    """
    it runs for O(n) as only loop while runs from mid = 0 to high = n-1 ,
    and we only used few variables so space complexity is O(1)
    """


sorting(nums)
print(nums)
