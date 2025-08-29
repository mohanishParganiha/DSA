from math import ceil
piles = [3, 6, 7, 11]
h = 8


def minEatingSpeed(piles: list[int], h: int) -> int:
    min_eating_speed = float('inf')
    piles.sort()

    left = 1
    right = piles[-1]
    while left <= right:
        hrs_took = 0
        mid = (left + right)//2
        for pile in piles:
            hrs_took += ceil(pile/mid)

        if hrs_took <= h:
            right = mid - 1
            min_eating_speed = min(min_eating_speed, mid)
        else:
            left = mid + 1

    return min_eating_speed


print(minEatingSpeed(piles, h))
