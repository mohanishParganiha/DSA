s = "barfoothefoobarman"
words = ["foo","bar"]

window_size = len(words[0])
seen_map = dict()
# i = 0
# left = 0
# right = 0


# while right < len(s):
#     if right - left == window_size:
#         left = right


#     right += 1

left = 0
right = left + window_size 

for word in words:
    while right < len(s):
        if s[left:right] == word:
            print(left)
            left = right
            right = left + window_size

