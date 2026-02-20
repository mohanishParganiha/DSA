n = 0


def climbingStaris(n):
    def recursion(n):
        if n == 0:
            return 1

        if n == 1:
            return 1

        return recursion(n-1) + recursion(n-2)
    return recursion(n)


print(climbingStaris(n))


def climbingStaris(n):
    cache = {}

    def memoization(n):
        if n == 0:
            return 1

        if n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = memoization(n-1) + memoization(n-2)
        return cache[n]

    return memoization(n)


print(climbingStaris(n))


def climbingStaris(n):
    def tabulation(n):
        if n == 0:
            return 1
        if n == 1:
            return 1
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
    return tabulation(n)


print(climbingStaris(n))
