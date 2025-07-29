height = [0,1,0,2,1,0,1,3,2,1,2,1]

def containWater(height):
    max_left = dict()
    max_right = dict()
    
    max_L = -1
    max_r = -1
    L = 0
    R = len(height)-1
    while L < len(height) and R > -1:

        if height[L] > max_L:
            max_L = height[L]
        max_left[L] = max_L
        if height[R] > max_r:
            max_r = height[R]
        max_right[R] = max_r

        L += 1
        R -= 1
    count = 0
    for i in range(len(height)):
        count += min(max_left[i],max_right[i])-height[i]

    return count
print(containWater(height))