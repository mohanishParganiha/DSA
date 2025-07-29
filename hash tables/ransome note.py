from collections import Counter

ransomeNote = "aa"
magazine = "aab"

def canConstruct(ransomeNote,magazine):
    ransome = Counter(ransomeNote)
    mag = Counter(magazine)

    for k in ransome:
        if mag[k] < ransome[k]  :
            return False
        
    return True

print(canConstruct(ransomeNote,magazine))