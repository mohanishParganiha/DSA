land = [[0, 1], [1, 0]]


def findGroupsOfFarmland(land: list[list[int]]) -> list[list[int]]:
    """to find all the farm land we have some contraints ,
            1)all the numbers are either 1 or 0
            2)no farmland is 4 directionally adjacent to each other ,
            3)to find  a square in grid , we can look at top left and bottom right corner,
                3.1)top_left corner will have smallest coordinates in that farmland,
                3.2)similarly , bottom right corner will have largest coordinates in that farmland.
    """
    rows = len(land)
    cols = len(land[0])

    top_left = (float('inf'), float('inf'))

    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols or land[x][y] == 0 or land[x][y] == -1:
            return

        bottom_row = max(x, bottom_right[0][0])
        bottom_col = max(y, bottom_right[0][1])
        bottom_right[0] = (bottom_row, bottom_col)
        # mark as seen
        land[x][y] = -1
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(x+dr, y+dc)
    ans = []
    for i in range(rows):
        for j in range(cols):
            bottom_right = [(float('-inf'), float('-inf'))]
            if land[i][j] == 1:
                top_left = (i, j)
                dfs(i, j)
                ans.append(
                    [top_left[0], top_left[1], bottom_right[0][0], bottom_right[0][1]])

    return ans


print(findGroupsOfFarmland(land))
