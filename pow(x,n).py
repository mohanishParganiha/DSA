x = 2.00000
n = -20


def pow(x,n):
    temp = n
    n = abs(n)

    if n == 0:
        return  1.0
    if x == 0:
        return 0.0
    if n == 1:
        return x
    
    if n % 2 != 0:
        mid_point = (n+1)/2.0 
    else:
        mid_point = n / 2.0

    ans = pow(x,n-mid_point) * pow(x,mid_point)

    if temp < 0:
        return (1/ans)

    return ans

print(pow(x,n))
