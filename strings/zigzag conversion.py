s = "AB"
numRows = 1

dir = -1
row = 0
ans = ['']*numRows
for char in s:
    if row == 0 or row == numRows-1:
        dir *= -1
    ans[row] += char
    row += dir

print(''.join(ans))