nums = [-1]
k  = 1

max_avg = 0
for i in range(len(nums)):
    avg = 0
    if i+k >len(nums):
        break
    avg = sum(nums[i:i+k])/float(k)
    max_avg = max(max_avg,avg)

print(max_avg)