s = "is2 sentence4 This1 a3"

s = s.split(" ")
word_list = [-1]*len(s)

for char in s:

    word_list[int(char[-1])-1] = char[0:-1]

sentence = " ".join(word_list)

print(sentence)
