import heapq

nums = [1, 2, 5, 2, 3]
target = 2


def findTargetIndices(nums, target):

    heapq.heapify(nums)  # O(n)
    ans = []

    for i in range(len(nums)):  # O(n)
        if heapq.heappop(nums) == target:
            ans.append(i)
    return ans


print(findTargetIndices(nums, target))
