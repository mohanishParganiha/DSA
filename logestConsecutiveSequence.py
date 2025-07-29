
from collections import Counter


nums = [100,4,200,1,3,2]
def longestConsecutive(nums):

    t_set = set(nums)
    max_length = 0

    if len(t_set) < 1:
        return 0
    elif  len(t_set) == 1:
        return 1

    for i in t_set:

        if not i-1 in t_set: #check if i-1 is in set , if not then i is the start of sequence 

            length = 0
            while i + length in t_set: #loop to check if i+1, i+2, i+3 ,,,, are in set  # make sure that you check the number of time loop is running , if we use < > == we might run out of index 

                length += 1 
                max_length = max(max_length,length)

    return max_length
print(longestConsecutive(nums))