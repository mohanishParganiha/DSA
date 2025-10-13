"""
give:
    1) we have integer arrya contains [x,y], so for ith  poin we have [Xi,Yi]
    2) we are given integer k , return k number of points which are closest to origin(0,0)
    3) euclidean distance = sqrt((x1-x2)^2 + (y1-y2)^2)

ways to solve this problem,
    -> we can use a min heap of [distance,[x,y]]
    -> use loop to pop k number of element and return them in a list


"""

from math import sqrt
import heapq


def kClosest(points: list[list[int]], k: int) -> list[list[int]]:

    min_heap = [[sqrt(point[0]**2 + point[1]**2), [point[0], point[1]]]
                for point in points]
    heapq.heapify(min_heap)
    return [heapq.heappop(min_heap)[1] for _ in range(k)]


points = [[1, 3], [-2, 2]]
k = 1

print(kClosest(points, k))
