board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
"""we can solve this using nested loop in brute foce way,
another way to solve this is using dfs from border,
? why not from center but why from border:
    we are looking for regions connected to borders ,thus best solution is to start at border not at center and expand outward ( it reduces calculataion and checking )
methodology:
we start at border 'O's and start dfs inward ,
we store every connectd 'O's  in safe_set as (i,j)
at last we conver every point to 'X' except for points in safe_set

the base case for dfs is if we reach the boundary"""


def solve(board: list[list[str]]) -> None:
    rows = len(board)
    cols = len(board[0])
    safe_set = set()

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] == "X":
            return

        if (i, j) in safe_set:
            return

        safe_set.add((i, j))
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            dfs(i+dr, j+dc)

    for j in range(cols):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[rows-1][j] == 'O':
            dfs(rows-1, j)

    for i in range(rows):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][cols-1] == 'O':
            dfs(i, cols-1)

    for i in range(rows):
        for j in range(cols):
            if (i, j) not in safe_set:
                board[i][j] = 'X'


for rows in board:
    print(rows)


solve(board)
print("\n")

for rows in board:
    print(rows)
