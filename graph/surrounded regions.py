from collections import deque
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

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] == "X" or board[i][j] == "M":
            return

        board[i][j] = "M"
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
            if board[i][j] != "M":
                board[i][j] = "X"
            else:
                board[i][j] = 'O'


board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

for rows in board:
    print(rows)


solve(board)
print("\n")

for rows in board:
    print(rows)

board = [["O"]]
solve(board)
print(board)
board = [["X"]]
solve(board)
print(board)
board = [["O", "O"], ["O", "O"]]
solve(board)
print(board)


def solveBfs(board: list[list[str]]) -> None:
    rows = len(board)
    cols = len(board[0])

    queue = deque()

    # iterate over edges and add all the "O" to queue
    for row in range(rows):
        if board[row][0] == "O":
            queue.append((row, 0))
            board[row][0] = "M"
        if board[row][cols-1] == "O":
            queue.append((row, cols-1))
            board[row][cols-1] = "M"

    for col in range(cols):
        if board[0][col] == "O":
            queue.append((0, col))
            board[0][col] = "M"

        if board[rows-1][col] == "O":
            queue.append((rows-1, col))
            board[rows-1][col] = "M"

    while queue:
        i, j = queue.popleft()
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= i+dr < rows and 0 <= j+dc < cols and board[i+dr][j+dc] == "O":
                board[i][j] = "M"
                queue.append((i+dr, j+dc))

    for i in range(rows):
        for j in range(cols):
            if board[i][j] != "M":
                board[i][j] = "X"
            else:
                board[i][j] = "O"


board = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]

for rows in board:
    print(rows)


solve(board)
print("\n")

for rows in board:
    print(rows)

board = [["O"]]
solve(board)
print(board)
board = [["X"]]
solve(board)
print(board)
board = [["O", "O"], ["O", "O"]]
solve(board)
print(board)
