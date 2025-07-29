s = "the sky is blue"
s = s.split(' ')
strings = []
for i in range(len(s)-1,-1,-1):
    if s[i] != '':
        strings.append(s[i])
print(' '.join(strings))
