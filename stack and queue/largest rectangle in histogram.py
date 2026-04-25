def largestRectangleArea(heights) -> int:
    max_height = 0
    stack = []

    # iterate over indexes
    for i in range(len(heights)):
        while stack and heights[stack[-1]] > heights[i]:
            height = heights[stack.pop()]
            if stack:
                width = i-stack[-1]-1
            else:
                width = i
            max_height = max(max_height, height*width)
        stack.append(i)

    if stack:
        length = len(heights)
        while stack and heights[stack[-1]] > -1:
            height = heights[stack.pop()]
            if stack:
                width = length-stack[-1]-1
            else:
                width = length
            max_height = max(max_height, height*width)
        stack.append(-1)
    return max_height


hist = [2, 1, 2]
print(largestRectangleArea(hist))
