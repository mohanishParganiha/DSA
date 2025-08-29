temperatures = [73, 74, 75, 71, 69, 72, 76, 73]


def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    ans = [0]*len(temperatures)
    for index, value in enumerate(temperatures):
        while stack and value > stack[-1][1]:
            t = stack.pop()
            ans[t[0]] = index-t[0]

        stack.append((index, value))

    return ans


print(dailyTemperatures(temperatures))
