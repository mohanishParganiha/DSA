nums = [1,3,0,0,2,0,0,4]


# count = 0

# for L in range(len(nums)):
#     if nums[L] != 0: continue
#     for R in range(L,len(nums),1):
#         if nums[R] != 0:
#             break
#         count += 1

# print(count)

count = 0
res = 0

for L in nums:
    if L == 0:
        count += 1
        res += count
    else:
        count = 0

print(res)