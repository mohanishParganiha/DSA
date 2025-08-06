import heapq

nums = [0, 2, 5, 3, 1, 4]

heapq.heapify(nums)  # O(n)

for i in range(len(nums)):  # O(n)
    print(heapq.heappop(nums))  # O(1) pop operations
