nums = [2,2,4,5]
k = 0

ans = 1 

sorted_array = sorted(nums)


minimum = 0
maximum = 0

while maximum < len(sorted_array):
    if not sorted_array[maximum] - sorted_array[minimum]  <= k:
        minimum = maximum
        ans += 1
        continue

    maximum += 1


print(ans)
