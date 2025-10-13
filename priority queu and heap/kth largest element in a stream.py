import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.min_heap = [float('-inf')]
        heapq.heapify(self.min_heap)
        for num in nums:
            if len(self.min_heap) < self.k:
                if num >= self.min_heap[0]:
                    heapq.heappush(self.min_heap, num)
            else:
                if num >= self.min_heap[0]:
                    heapq.heapreplace(self.min_heap, num)

    def add(self, val: int) -> int:
        if val >= self.min_heap[0]:
            heapq.heapreplace(self.min_heap, val)
            return self.min_heap[0]

        return self.min_heap[0]


min_heap1 = KthLargest(3, [4, 5, 8, 2])
print(min_heap1.add(3))
print(min_heap1.add(5))
print(min_heap1.add(10))
print(min_heap1.add(9))
print(min_heap1.add(4))
