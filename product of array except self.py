nums = [1,2,3,4,0]
    
def product(nums):
    suffix_product = []
    prefix_product = []
    ans_arr = []
    # calculating the suffix product of the nums array , i.e. [1,2,3,4] -> [1,1*2,1*2*3,1*2*3*4,...]
    product = 1
    for i in nums:
        product *= i
        suffix_product.append(product)

    #calculating the prefix product of the nums array, i.e. [1,2,3,4] -> [1*2*3*4,2*3*4,3*4,4,...]
    product = 1
    for i in range(len(nums)-1,-1,-1):
        product *= nums[i]
        prefix_product.append(product)

    prefix_product.reverse() # the prefix array is [4,12,24,24] but we want the reverse of this according to the above comment 

    # calculating the final product of array where the nums[i] = nums[i-2 * i-1 * i+1 * i+2 * i+3 * ...,] except i th index it self 

    # formulat is product at i , p[i] = suffix[i-1]*prefix[i+1]
    product = 1
    for i in range(len(nums)):
        if i == 0: # we are handeling edge cases when i == 0, i.e. starting of array
            product =  1 * prefix_product[i+1]
        elif i == len(nums)-1: # handeling edge cases when i == len(nums)-1 , i.e ending of array
            product = suffix_product[(len(nums)-1)-1] * 1 
        else:
            product = suffix_product[i-1] * prefix_product[i+1]
        ans_arr.append(product)
    return ans_arr

print(product(nums))