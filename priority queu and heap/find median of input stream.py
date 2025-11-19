import heapq


class MedianFinder:

    def __init__(self):
        self.smaller_half = []
        heapq.heapify(self.smaller_half)
        self.larger_half = []
        heapq.heapify(self.larger_half)

    def addNum(self, num: int) -> None:
        if not self.smaller_half:
            heapq.heappush(self.smaller_half, -num)
        if num > -self.smaller_half[0]:
            heapq.heappush(self.larger_half, num)
        else:
            heapq.heappush(self.smaller_half, -num)

        # rebalnce if? needed
        if len(self.smaller_half) < len(self.larger_half):
            heapq.heappush(self.smaller_half, -heapq.heappop(self.larger_half))
        elif len(self.smaller_half) > len(self.larger_half)+1:
            heapq.heappush(self.larger_half, -heapq.heappop(self.smaller_half))

    def findMedian(self) -> float:
        if (len(self.smaller_half) + len(self.larger_half)) % 2 == 0:
            return ((-self.smaller_half[0]) + self.larger_half[0]) / 2
        else:
            return (-self.smaller_half[0])


obj = MedianFinder()
obj.addNum(1)
obj.addNum(2)
print(obj.findMedian())
obj.addNum(3)
print(obj.findMedian())
