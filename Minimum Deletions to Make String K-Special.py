from collections import Counter

word =  "dabdcbdcdcd"
k = 2

freq = [i for i in Counter(word).values()]

ans = float('inf')

for i in range(len(freq)):
    min_deleition = 0
    for j in range(len(freq)):
        if i == j :
            continue

        if freq[j] < freq[i]:
            min_deleition += freq[j]

        elif abs(freq[j] - freq[i])>k :
            min_deleition += abs(freq[j]-freq[i] -k)
            
    ans = min(ans,min_deleition)

