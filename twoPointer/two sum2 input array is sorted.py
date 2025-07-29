from collections import defaultdict
numbers = [-1,0]
target = -1

def twoSum(nums,target):
    
    L = 0
    R = len(numbers)-1

    while L < R:

        if numbers[L] + numbers[R] < target:
            L += 1
        elif numbers[L] + numbers[R] > target:
            R -= 1
        else:
            return [L+1,R+1]
    return None

print(twoSum(numbers,target))
