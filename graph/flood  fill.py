from collections import deque


def floodFill(image: list[list[int]], sr: int, sc: int, color: int):
    if image[sr][sc] == color:
        return image

    def bfs(sr, sc):
        queue = deque()
        queue.append((sr, sc))
        starting_color = image[sr][sc]
        image[sr][sc] = color
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c = r+dr, c+dc
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]) and image[new_r][new_c] == starting_color:
                    image[new_r][new_c] = color
                    queue.append((new_r, new_c))
    return bfs(sr, sc)


image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
sr = 1
sc = 1
color = 2

floodFill(image, sr, sc, color)
for row in image:
    print(row)
