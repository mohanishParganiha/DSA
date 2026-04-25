g = [10, 9, 8, 7]

s = [5, 6, 7, 8]


def findContentChildren(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()

    content_children = 0
    while s and g:
        biggest_cookie = s.pop()
        while g:
            greediest_child = g.pop()
            if biggest_cookie >= greediest_child:
                content_children += 1
                break

    return content_children


print(findContentChildren(g, s))
