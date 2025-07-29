nums = [0,1,1,1,1,1,0,0,0] # in prefix sum if we get sum equal at 2 different indices 
            #then the number of one's is equal to number of zeros between those indices

prefix_sum = 0
hashmap = dict()
max_lenght = 0

for i, n in enumerate(nums):
    if n == 0:
        prefix_sum -= 1 # we are decreasing 1 from prefix sum everytime we get a zero
    else:
        prefix_sum += 1 # we are adding 1 from prefix sum everytime we get a one

    if prefix_sum in hashmap: # if the prefix sum is already in map
        max_lenght = max(max_lenght,i-hashmap[prefix_sum]) # if so then check the max of max_length (before ) and i-hashmap[prefixlength](after)

    hashmap[prefix_sum] = i

print(max_lenght)