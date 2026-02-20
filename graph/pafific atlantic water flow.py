"""given m x n grid  that borders both pacific ocean and atlantic ocean.
each cell represent height above the sea level , i.e. height[i][j] is height at point i,j
when rain fall water can flow from (i,j) to its neighbors if height[i][j] is greater than equal to its neighbors
for this we can use dfs but we will move invards from edges, this way we wont have to check every point in middle.

steps:
1) we will have two sets containing coordinates (i,j) pacific sets and atlantic sets,
2)we will start from edges coordinates then move invard ,for this
    we will check all four direction , and make sure  we are not out of bounds
    and also check if we have not already visited this point.
    we will move invard if height[i][j] is less than equal to height at  next i,j
    we will use dfs
"""


def pacificAtlantic(heights: list[list[int]]) -> list[list[int]]:
    pacific_set = set()
    atlantic_set = set()
    rows = len(heights)
    cols = len(heights[0])

    def dfs(i, j, ocean_set: set):
        if (i, j) in ocean_set:
            return

        ocean_set.add((i, j))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i+dr < rows and 0 <= j+dc < cols and heights[i+dr][j+dc] >= heights[i][j]:
                dfs(i+dr, j+dc, ocean_set)

    # 1'st  row
    for col in range(cols):
        dfs(0, col, pacific_set)

    # 1'st col
    for row in range(rows):
        dfs(row, 0, pacific_set)

    # last  row
    for col in range(cols):
        dfs(rows-1, col, atlantic_set)

    # last col
    for row in range(rows):
        dfs(row, cols-1, atlantic_set)

    return list(pacific_set.intersection(atlantic_set))


heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [
    2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacificAtlantic(heights))
