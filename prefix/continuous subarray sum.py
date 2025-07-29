nums = [5,0,0,0]
k = 3

def check(nums,k):
    if len(nums) < 2:
        return False
    prefix_sum = 0
    remainder_map = {0:-1}
    count = 0

    for i ,n in enumerate(nums):
        prefix_sum += n
        remainder  = prefix_sum % k

        if remainder in remainder_map:
            if i - remainder_map[remainder] > 1:
                return True
        else:
            remainder_map[remainder] = i

    return False

print(check(nums,k))