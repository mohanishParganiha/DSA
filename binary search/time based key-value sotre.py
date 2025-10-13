

class TimeMap:

    def __init__(self):
        self.timeMap = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append([timestamp, value])
        else:
            self.timeMap[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            less_than_timestamp_value = ''
            left = 0
            right = len(self.timeMap[key]) - 1
            while left <= right:
                mid = (left + right) // 2

                if self.timeMap[key][mid][0] <= timestamp:
                    less_than_timestamp_value = self.timeMap[key][mid][1]

                if self.timeMap[key][mid][0] > timestamp:
                    right = mid - 1
                else:
                    left = mid + 1

            return less_than_timestamp_value


timeMap = TimeMap()
timeMap.set('foo', 'bar', 1)
print(timeMap.get('foo', 1))
