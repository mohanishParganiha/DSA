nums =[1,5,0,4,1,3]

def find(nums):

    first = second = float("inf")
    for n in nums:
        if n <= first:
            first = n
        elif n <= second:
            second = n
        else:
            return True
        
    return False

print(find(nums))