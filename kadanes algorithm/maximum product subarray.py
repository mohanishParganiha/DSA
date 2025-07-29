nums = [0,2]
def maxProduct(nums):
    max_product = float('-inf')
    curr_max_product = 1

    i = 0
    while i < len(nums):

        curr_max_product *= nums[i]

        if curr_max_product  >= max_product:
            max_product = max(max_product , curr_max_product)
        else:
            curr_max_product = 1
            
        i += 1

    return max_product


print(maxProduct(nums))