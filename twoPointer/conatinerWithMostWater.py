height = [1,1]

def solution(height):
    L = 0
    R = len(height)-1
    maximum = 0

    while L < R:
        vol = min(height[L],height[R]) * (R-L)

        if maximum < vol:
            maximum = max(maximum,vol)

        if height[L] < height[R]:
            L += 1
        elif height[R] < height[L]:
            R -= 1
        elif height[L] == height[R]:
            L += 1

        if L == R:
            return maximum
        

    return maximum

print(solution(height))