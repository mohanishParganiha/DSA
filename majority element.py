nums = [3, 2, 3]
# condition for majority element is f(nums[i]) > n/2 where n is size of array 

counter_set = {}
max_count  = 0
max_element = 0

for num in nums:
    if num in counter_set:
        counter_set[num] += 1
    else:
        counter_set[num] = 1
    
    if counter_set[num] >= max_count:
        max_count =  counter_set[num]
        max_element = num
    

print(max_count)
print(max_element)



# second approach 

from collections import Counter

counter = Counter(nums).most_common(1)
print(counter[0][0])