import heapq
from collections import Counter
string = 'aab'


def reorganizeString(s: str) -> str:
    max_heap = [(-f, char) for char, f in Counter(s).items()]
    heapq.heapify(max_heap)
    ans = ""
    prev = (0, '')
    while max_heap:
        freq, char = heapq.heappop(max_heap)

        ans += char
        # reduce requency as freq is in negetive , so  +1 will reduce it (-3+1 = -2)

        if prev[0] < 0:
            heapq.heappush(max_heap, prev)

        freq += 1
        prev = (freq, char)

    if prev[0] < 0:
        return ""

    return ans


print(reorganizeString(string))
