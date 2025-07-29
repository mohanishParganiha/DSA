nums = [1,2,3,4]
n = 4
left = 1
right = 5

new_arr = []
count = 0

for L  in range(n):             # O(n)
    for R in range(L,n,1):    # O(n)
        sum = nums[L] + nums[R]
        if sum <= new_arr[R]:
            new_arr.insert(R,sum)
        else:
            new_arr.insert()