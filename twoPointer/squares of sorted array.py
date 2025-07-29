nums = [-4,-1,0,3,10]

sqr_arr = []
L = 0
R = len(nums)-1
while L <= R:
    if abs(nums[L]) > abs(nums[R]):
        sqr_arr.append(nums[L]**2)
        L += 1

    else:
        sqr_arr.append(nums[R]**2)
        R -= 1

    
print(sqr_arr[::-1])