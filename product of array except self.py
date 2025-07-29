nums = [1,2,3,4,0]
    
def product(nums):
    prefix = [1]*len(nums)
    suffix = [1]*len(nums)

    for i in range(1,len(nums)):
        try:
            prefix[i] = prefix[i-1] * nums[i-1]
        except:
            pass

    for j in range(len(nums)-2,-1,-1):
        try:
            suffix[j] = suffix[j+1] * nums[j+1]
        except:
            pass
    answer = [prefix[i] * suffix[i] for i in range(len(nums))]

    print(answer)
product(nums)