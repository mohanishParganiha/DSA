n = 3


def generateParentheses(n) -> list[str]:
    """
        1/string_length = n*2 (2 cause we need valid pair ,so n pair will have n*2 number of char,
                            for eg. n= 3 then s = "((()))", here length of string is 3*2 = 6)
        2/number_of_open_parentheses = string_lenght/2,
        3/number_of_close_parentheses = string_length/2

        4/we start with string = ""
        5/every time we check if we can add open/close parentheses,
                if we dont have open parenthese we cant add closing parentheses ,
                we can check if we have open parentheses by checking (2),(3),
                if number_of_open_parentheses is less than number_of_close_parentheses then we
                    have extra  open parentheses
        6/every time we add open/close parentheses we decreases (2),(3) by one
        7/ we use recursion for this and save the leaf nodes once all the lenght of
                ans string is equal to string_length


    """
    res = []
    ans_stack = []

    def backtrack(openN, closeN):

        if openN == closeN == n:
            res.append("".join(ans_stack))

        if openN < n:
            ans_stack.append('(')
            backtrack(openN+1, closeN)
            ans_stack.pop()

        if closeN < openN and closeN < n:
            ans_stack.append(')')
            backtrack(openN, closeN+1)
            ans_stack.pop()

    backtrack(0, 0)
    return res


print(generateParentheses(n))
