from collections import defaultdict
nums = [4,5,0,-2,-3,1]
k = 5



prefix_sum = 0
mod_freq = defaultdict(int)
mod_freq[0] = 1
count = 0

for n in nums:
    prefix_sum += n
    mod = prefix_sum % k
    if mod < 0:
        mod += k
        
    count +=  mod_freq[mod]
    mod_freq[mod] += 1

print(count)