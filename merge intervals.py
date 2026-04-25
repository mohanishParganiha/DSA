intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]


def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(reverse=True, key=lambda x: x[0])

    ans = []
    while intervals:
        start, end = intervals.pop()

        while intervals and (intervals[-1][0] <= end <= intervals[-1][1] or start <= intervals[-1][0] <= end):
            next_start, next_end = intervals.pop()
            end = max(end, next_end)

        ans.append([start, end])
    return ans


print(merge(intervals))
