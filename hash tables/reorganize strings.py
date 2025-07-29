from collections import Counter
import heapq

s = "aaab"
def find(s):
    max_heap = [(-freq,char) for char,freq in Counter(s).items()]
    heapq.heapify(max_heap)
    prev = (0,'')
    result = []

    while max_heap:
        freq ,char = heapq.heappop(max_heap)

        result.append(char)

        if prev[0] < 0:
            heapq.heappush(max_heap,prev)

        freq += 1
        prev=(freq,char)

    if prev[0] < 0:
        return ""

    result = ''.join(result)
    return result

print(find(s))