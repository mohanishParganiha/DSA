from collections import defaultdict
nums = [2,7,11,15]
target = 9


def twoSum(nums:list[int],target:int)-> list[int]:
    seen_hashMap = defaultdict(int)

    i = 0
    while i < len(nums):
        new_target = target - nums[i]
        if new_target in seen_hashMap:
            return [seen_hashMap[new_target],i]
        seen_hashMap[nums[i]] = i       

        i += 1

print(twoSum(nums=nums,target=target))