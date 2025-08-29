tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]

# we add the tokens in a stack ,
# as soon as we encounter a operator token we perform the operation on last 2 tokens and push the ans in there place


def evalRPN(token: list[str]) -> int:
    stack = []
    operators = set(['-', '+', '/', '*'])
    for token in tokens:
        if token not in operators:
            stack.append(int(token))
        else:
            if token == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(b+a)
            elif token == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif token == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(b*a)
            elif token == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))

    return stack.pop()


print(evalRPN(tokens))
