nums = [9,5,7,8,7,9,8,2,0,7]

nums.sort()

i = 0
j = len(nums)-1

avg_set = set()

while i<j:
    avg_set.add((nums[i]+nums[j])/2)
    i += 1
    j -= 1
print(len(avg_set))

