fruits = [1,2,3,2,2,4]


# we are gonna use 2 pionter dynamic window approach 
# we will move the i to right on fixed window size of 2 , 
# if the next fruit is same as in basket(hashmap size of 2) \
#       then we will expand the window to get the same fruit
# and if the next fruit is not the same , \
#       then we reduce the size of window to take out one type of furit 
#        untill one basket is empty , 
#we keep track of max number of fruits in the basket(hashmap)


def totalFruit(fruits):
    basket = {}
    window_size = 0

    L  = 0
    R = 0

    while R < len(fruits):
        if fruits[R] not in basket:
            if len(basket) < 2:
                basket[fruits[R]] = 1
            else:
                if basket[fruits[L]] > 1:
                    basket[fruits[L]] -= 1
                else:
                    del basket[fruits[L]]
                L += 1
                continue
            
        else:
            basket[fruits[R]] += 1
        
        R += 1
        window_size = max(window_size,R-L)

    return window_size