from collections import deque


def orangesRotting(grid):
    rows = len(grid)
    cols = len(grid[0])
    fresh = 0
    queue = deque()

    # add all the rotten oranges to the queue
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 2:
                queue.append((i, j, 0))
            # count the number of fresh oranges
            if grid[i][j] == 1:
                fresh += 1
    # start bfs with queue
    time = 0
    while queue:
        # pop the first item
        i, j, time = queue.popleft()
        # check the 4 direction neighbours
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            # check the bounds and if orange at i,j is fresh
            if 0 <= i+dr < rows and 0 <= j+dc < cols and grid[i+dr][j+dc] == 1:
                # if fresh turn it into rotten so we dont process it again
                grid[i+dr][j+dc] = 2
                # add this point to queue
                queue.append((i+dr, j+dc, time+1))
                # reduce the fresh oranges by 1
                fresh -= 1

    return time if fresh == 0 else -1


grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
print(orangesRotting(grid))
