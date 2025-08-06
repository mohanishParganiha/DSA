height = [1,8,6,2,5,4,8,3,7]

left = 0
right = len(height)-1
ans = 0
while left < right:
    ans = max(ans,min(height[left],height[right])*((right-left)))#caculate area and choose max 

    if height[left] > height[right]:
        #move right if right is smaller 
        right -= 1
    elif height[right] > height[left]:
        #move left if left is smaller
        left += 1

    else: #if both are same then choose which of the next one is bigger i.e height[left+1] > height[right+1]
        if height[left+1] >= height[right]:
            left += 1
        else:
            right -= 1


print(ans)