n = 43261596
n = bin(n)[2:]

ans = ['']*len(n)
L = 0
R = len(n)-1
while L < R:
    ans[L] = n[R]
    ans[R] = n[L]
    L += 1
    R -= 1
print(''.join(ans))