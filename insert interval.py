def insert(intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
    output = []
    for i in range(len(intervals)):
        new_start = newInterval[0]
        new_end = newInterval[1]
        curr_start = intervals[i][0]
        curr_end = intervals[i][1]

        if new_end < curr_start:
            output.append(newInterval)
            output.extend(intervals[i:])
            return output
        elif curr_end < new_start:
            output.append(intervals[i])
        else:
            newInterval = [min(new_start, curr_start), max(new_end, curr_end)]
    output.append(newInterval)
    return output


intervals = [[3, 5], [12, 15]]
newInterval = [6, 6]
print(insert(intervals, newInterval))
