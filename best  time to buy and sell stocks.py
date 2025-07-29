prices = [2,1,2,0,1]

maximum_profit = 0
L = 0
R = 1

while R < len(prices):
    if prices[L] < prices[R]:
        maximum_profit = max( prices[R]-prices[L],maximum_profit)
    else:
        L = R
    
    R += 1




print(maximum_profit)
    
    

    
