nums = [1,1,1,1]

pairs = dict()

left = 0
right = 1

while left < len(nums):
    if right >=len(nums):
        left += 1
        right = left + 1
        continue
    if nums[left] == nums[right]:
        pairs[(left,right)]=[nums[left],nums[right]]
        
    right += 1

print(len(pairs))