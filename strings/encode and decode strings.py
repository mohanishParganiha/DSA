from collections import Counter


a = ["neet","code","love","you"]

def encode(strs:list):
    for i in strs:
        temp = Counter(i).most_common(len(i))
        print(temp)
        temp_list = []
        temp_str = ''.join(temp)
        temp_list.append(temp_str)
        print(temp_list)

encode(a)