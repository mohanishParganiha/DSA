from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagram(strs:list[str])-> list[str]:
    seen_map = defaultdict(list)
    for word in strs:
        sorted_word = tuple(sorted(word))
        seen_map[sorted_word].append(word)
    return list(seen_map.values())
print(groupAnagram(strs))