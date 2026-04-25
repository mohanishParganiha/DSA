path = "/home/"


def simplifyPath(path) -> str:

    list1 = [char for char in path.split('/') if char != '']
    print(list1)

    stack = []
    for directory in list1:
        if directory == '..':
            if stack:
                stack.pop()
            continue
        if directory == '.':
            continue
        stack.append(directory)

    path = '/'.join(stack)
    return '/'+path


print(simplifyPath(path))
