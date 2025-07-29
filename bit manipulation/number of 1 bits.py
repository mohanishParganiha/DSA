
n = 11

# ans = []
# for i in range(0,n+1):
#     i = (bin(i)[2:])
#     a = 0
#     for j in i:
#         a += int(j)
#     ans.append(a)
# print(ans)

res = 0
while n:
    res += n % 2
    n = n>> 1
print(res)