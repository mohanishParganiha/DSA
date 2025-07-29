nums = [0,0,1,1,1,1,2,3,3]

# remove duplicate elements and leave 2 behind , soo remvoe one "1" from above it becomes 1,1,2,2,3
#use 2 pointers L, R

L = 0
R = L + 1
step = 2
while L  < len(nums) and R < len(nums):
    if nums[L] == nums[R] and R-L < step: # if both are equal take a right step with right pointer
        R += 1
    elif nums[L] == nums[R] and R-L == step:# if both are equal and  the difference between the two is 2
        nums.pop(R-1)            # it means that there is one more duplicate between the two pointers remove that
                        
    else:
        L = R
        R = L+1

print(nums)