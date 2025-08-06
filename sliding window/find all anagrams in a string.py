from collections import Counter


def isAnagram(s,p_count):
    s_count = Counter(s)

    return (s_count == p_count)  
        


s = "cbaebabacd"
p = "abc"
def findAllAnagramInString(s:str,p:str)->list[int]:
    p_counter = Counter(p)
    s_counter = Counter()
    window_size = len(p)
    ans_list = []
    for i in range(len(s)):

        s_counter[s[i]] += 1
        
        if i >= window_size:
            if s_counter[s[i-window_size]] == 1:
                del s_counter[s[i-window_size]]
            else:
                s_counter[s[i-window_size]] -= 1
        
        if s_counter == p_counter:
            ans_list.append(i-window_size+1)

    return ans_list


print(findAllAnagramInString(s,p))