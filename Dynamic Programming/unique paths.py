m = 3
n = 7


def uniquePath(m, n):  # type: ignore

    def recursion(x, y):
        if x == m-1 and y == n-1:
            return 1

        if x >= m or y >= n:
            return 0

        return recursion(x+1, y) + recursion(x, y+1)

    return recursion(0, 0)


print(uniquePath(m, n))


def uniquePath(m, n):  # type: ignore
    cache = {}

    def memoization(x, y):
        if x == m-1 and y == n-1:
            return 1
        if x >= m or y >= n:
            return 0

        if (x, y) in cache:
            return cache[(x, y)]

        cache[(x, y)] = memoization(x+1, y) + memoization(x, y+1)
        return cache[(x, y)]
    return memoization(0, 0)


print(uniquePath(m, n))

m = 1
n = 1


def uniquePath(m, n):
    def tabulation():

        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        for j in range(n-2, -1, -1):
            dp[m-1][j] = dp[m-1][j+1]

        for i in range(m-2, -1, -1):
            dp[i][n-1] = dp[i+1][n-1]

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                dp[i][j] = dp[i+1][j] + dp[i][j+1]

        return dp[0][0]

    return tabulation()


print(uniquePath(m, n))
