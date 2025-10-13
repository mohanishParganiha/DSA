"""
give:
    1) array containes weight of stones , weight of ith stone = array[i]

    2) suppose two stones x and y , where x <= y ,
        we collide those two stones with each other , x -> y = z ,
        z = 0 if x == y,
        z = y-x if x != y

    3) at end there remains single stone return that stone ,

    ways to solve  ,
    -> first methond comes to mind is using max heap and
        1)take out y and x ,  y = first pop,x = second pop
        2)check if x == y, then y-x == 0 if so dont put anything back to max heap,
                 if x < y, put back y-x onto max heap ,
        3)save this y-x on both cases in a variable last_remaining_stone
        3) repeat everything untill the heap is empty ,  and return last_remaining_stone

"""
import heapq


def lastStoneWeight(stones: list[int]) -> int:
    stones = [-weight for weight in stones]
    heapq.heapify(stones)
    while len(stones) > 1:

        y = abs(heapq.heappop(stones))
        x = abs(heapq.heappop(stones))

        if x < y:
            heapq.heappush(stones, -(y-x))
    if len(stones) == 0:
        return 0
    return abs(heapq.heappop(stones))


stones = [2, 7, 4, 1, 8, 1]
print(lastStoneWeight(stones))
