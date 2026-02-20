coins = [5]
amount = 11


def coinChange(coins: list[int], target: int):  # type: ignore
    def recursion(target: int):
        if target == 0:
            return 0

        if target < 0:
            return float('inf')

        ans = float('inf')
        for coin in coins:
            ans = min(1 + recursion(target-coin), ans)  # type: ignore

        return ans

    result = recursion(target)
    if result == float('inf'):
        return -1
    return result


print(coinChange(coins, amount))


def coinChange(coins: list[int], target: int):  # type: ignore
    cache = {}

    def recursion(target: int):
        if target == 0:
            return 0

        if target < 0:
            return float('inf')

        if target in cache:
            return cache[target]

        ans = float('inf')
        for coin in coins:
            result = 1 + recursion(target-coin)
            ans = min(result, ans)  # type: ignore

        cache[target] = ans

        return cache[target]

    result = recursion(target)
    if result == float('inf'):
        return -1
    return result


print(coinChange(coins, amount))


def coinChange(coins: list[int], target: int):
    def tabulation():
        dp = [float('inf')]*(target+1)
        dp[0] = 0
        for i in range(1, target+1):
            min_coins = float('inf')
            for coin in coins:
                if i-coin >= 0:
                    min_coins = min(min_coins, dp[i-coin])
            dp[i] = 1 + min_coins
        if dp[target] == float('inf'):
            return -1
        return dp[target]
    return tabulation()


print(coinChange(coins, amount))
