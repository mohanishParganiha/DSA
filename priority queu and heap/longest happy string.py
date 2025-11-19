import heapq


def longestDiverseString(a: int, b: int, c: int) -> str:

    max_heap = [(-freq, char)
                for freq, char in [(a, 'a'), (b, 'b'), (c, 'c')] if freq > 0]
    heapq.heapify(max_heap)
    ans = ""
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        while abs(freq) > 0 and not (len(ans) >= 2 and ans[-1] == ans[-2] == char):
            ans += char
            freq += 1

        if len(ans) >= 2 and ans[-1] == ans[-2] == char:
            prev = (freq, char)
            if not max_heap:
                heapq.heappush(max_heap, prev)
                break
            freq, char = heapq.heappop(max_heap)
            ans += char
            freq += 1
            heapq.heappush(max_heap, prev)
            if freq != 0:
                heapq.heappush(max_heap, (freq, char))

    return ans


print(longestDiverseString(a=1, b=1, c=7))
