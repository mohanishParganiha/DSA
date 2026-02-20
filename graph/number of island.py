def numIslands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(i, j):
        # Your code
        if grid[i][j] == '0':
            return

        if (i, j) in visited:
            return

        visited.add((i, j))
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if i+dr == rows or i+dr < 0 or j+dc == cols or j+dc < 0:
                continue
            dfs(i+dr, j+dc)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and (i, j) not in visited:
                dfs(i, j)
                count += 1

    return count


grid = [
    ['1', '1', '0'],
    ['1', '0', '1'],
    ['0', '1', '1']
]

print(numIslands(grid))
