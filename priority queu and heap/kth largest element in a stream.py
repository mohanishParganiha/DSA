import heapq


class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k_th = k
        # size of heap should be k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k_th:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        while len(self.min_heap) > self.k_th:
            heapq.heappop(self.min_heap)
        item = heapq.heappop(self.min_heap)
        heapq.heappush(self.min_heap, item)
        return item


min_heap1 = KthLargest(3, [4, 5, 8, 2])
print(min_heap1.add(3))
print(min_heap1.add(5))
print(min_heap1.add(10))
print(min_heap1.add(9))
print(min_heap1.add(4))
