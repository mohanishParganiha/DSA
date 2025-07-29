nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3

def find(nums,k):

    left = 0

    for right in range(len(nums)):
        
        if nums[right] == 0:
        
            k -= 1

        if k < 0:
            if nums[left] == 0:
                k += 1

            left += 1




    return right - left + 1

print(find(nums,k))