nums = [10, 22, 9, 33, 21, 50, 41, 60, 80]


def lengthOfLIS(nums: list[int]) -> int:  # type: ignore

    def recursion(idx):
        if idx == len(nums):
            return 0
        result = 0
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:
                result = max(result, recursion(i))
        return 1 + result
    solution = 0
    for i in range(len(nums)):
        solution = max(solution, recursion(i))

    return solution


print(lengthOfLIS(nums))


def lengthOfLIS(nums: list[int]) -> int:  # type: ignore
    cache = {}

    def memoization(idx):
        if idx == len(nums):
            return 0

        if idx in cache:
            return cache[idx]

        result = 0
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:
                result = max(result, memoization(i))
        cache[idx] = 1 + result
        return cache[idx]
    solution = 0
    for i in range(len(nums)):
        solution = max(solution, memoization(i))

    return solution


print(lengthOfLIS(nums))


def lengthOfLIS(nums: list[int]) -> int:  # type: ignore
    n = len(nums)
    if n == 0:
        return 0

    def tabulation():
        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1+dp[j])
        return max(dp)
    return tabulation()


print(lengthOfLIS(nums))

"""we can further increase the performance be deciding which index we should start searching from
a sequence : can be defined as a list of numbers where number at i is less than i+1,
similarly a start of sequence can be found: if number smaller than i does not exist i.e i = 10 , if 9 exist at index less than i-1

step 1- create a copy of given array and sort it O(nlog(n))
step 2- find the starting of squences , use binary search to check if "nums[i]-1" exist in sorted array and
        is at index less than i , i.e. nums[i] -> index = binarySearch(nums[i]-1), if found check index < i
        if found then proceede with dp  memoization
step 3- at each step we take maximum

"""


def lengthOfLIS(nums: list[int]) -> int:  # type: ignore
    sorted_array = sorted(nums)

    def binarySearch(num) -> int:
        left = 0
        right = len(sorted_array)-1

        while left <= right:
            mid = (left+right) // 2

            if sorted_array[mid] == num:
                return mid

            if sorted_array[mid] > num:
                right = mid-1
            else:
                left = mid+1
        return -1

    cache = {}

    def memoization(idx):
        if idx == len(nums):
            return 0

        if idx in cache:
            return cache[idx]

        result = 0
        for i in range(idx+1, len(nums)):
            if nums[i] > nums[idx]:
                result = max(result, memoization(i))
        cache[idx] = 1 + result
        return cache[idx]
    solution = 0
    # implement binary search
    for i in range(len(nums)):
        binary_searched_num = binarySearch(nums[i]-1)
        if binary_searched_num > -1:
            if binary_searched_num > i:
                solution = max(solution, memoization(i))
    return solution


print(lengthOfLIS(nums))
