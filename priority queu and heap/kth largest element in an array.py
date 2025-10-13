"""
give:
    array with integers ,
    return kth largest element
    solve without sorting

ways to sovle:
    create a max_heap by heapq.heapify(),
    run a loop k time and pop items , return the last poped item
"""
import heapq


def findKthLargest(nums: list[int], k: int) -> int:
    max_heap = [-num for num in nums]
    heapq.heapify(max_heap)

    for _ in range(k-1):
        heapq.heappop(max_heap)

    return heapq.heappop(max_heap)
