nums = [-6,2,5,-2,-7,-1,3]
target = -2

count = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums),1):
        if nums[i] + nums[j] < target:
            count += 1
print(count)
