from collections import deque

grid = [
    [2147483647, -1, 0, 2147483647],
    [2147483647, 2147483647, 2147483647, -1],
    [2147483647, -1, 2147483647, -1],
    [0, -1, 2147483647, 2147483647]
]

# 2147483647 represents INF aka land , 0 represents treasure chest, -1 represents wate and cannot be traversed

"""so give we have a grid of size mxn 2d matrix , each coordinate is -1 or 0 or 2^31-1 ,
we need to modify the grid in place such that each coordinates are distance to treasure chests,
and we cannot travers over -1.

1) we can use nested loops to loop through each elements and calculate distance
2) we can use bfs  to traverse level by level and calculate distance
we will go with 2nd method ,
first we will add all the 0's to  queue , and propagate the bfs traversal in 4 directions

"""


def islandsAndTreasure(grid: list[list[int]]) -> list[list[int]]:
    queue = deque()
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 0:
                queue.append((i, j, 0))

    while queue:
        i, j, distance = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i+dr < rows and 0 <= j+dc < cols and grid[i+dr][j+dc] == 2147483647:
                grid[i+dr][j+dc] = distance + 1
                queue.append((i+dr, j+dc, distance+1))

    return grid


solution = islandsAndTreasure(grid)
for rows in solution:
    print(rows)
