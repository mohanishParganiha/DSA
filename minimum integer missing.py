nums = [1,2,0]


def find(nums):
    for n in range(len(nums)):
        if nums[n] < 0 :
            nums[n] = 0

    print(nums)

    for n in range(len(nums)):
        index = abs(nums[n]) -1
        if index in range(len(nums)):
            if nums[index] > 0:
                nums[index] *= -1
            elif nums[index] == 0:
                nums[index] = -(len(nums)+1)

    print(nums)

    for n in range(1,len(nums)+1):
        if nums[n-1] >= 0:
            return n
    
    return len(nums)+1

print(find(nums))