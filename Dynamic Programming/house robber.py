houses = [1, 3, 6, 3, 2, 1]

"""this is recursion way to solve this """


def recurse(idx):
    if idx < 0:
        return 0

    rob_current = recurse(idx-2, )+houses[idx]
    skip_to_next = recurse(idx-1)

    return max(rob_current, skip_to_next)


print(recurse(len(houses)-1))

"""this is top down memoization way to solve this """


def memoization(houses):
    cache = {}

    def helper(idx):
        if idx < 0:
            return 0

        if idx in cache:
            return cache[idx]

        rob_current = helper(idx-2)+houses[idx]
        skip_to_next = helper(idx-1)

        cache[idx] = max(rob_current, skip_to_next)

        return cache[idx]

    return helper(len(houses)-1)


print(memoization(houses))


"""this is bottom up dp tabulation , we store and calculate it in an array of same size as input array"""


def tabulation(houses):
    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    dp = [0]*len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i-2]+houses[i], dp[i-1])

    return dp[len(houses)-1]


print(tabulation(houses))


call_count = 0


def recurse_counted(idx):
    global call_count
    call_count += 1
    if idx < 0:
        return 0
    rob_current = recurse_counted(idx-2) + houses[idx]
    skip_to_next = recurse_counted(idx-1)
    return max(rob_current, skip_to_next)


def memoization_counted(idx, call_count):
    cache = {}
    call_count[0] += 1

    def helper(idx):
        call_count[0] += 1
        if idx < 0:
            return 0

        if idx in cache:
            return cache[idx]

        rob_current = helper(idx-2)+houses[idx]
        skip_to_next = helper(idx-1)

        cache[idx] = max(rob_current, skip_to_next)

        return cache[idx]

    return helper(len(houses)-1)


def tabulation_counted(idx):
    global call_count
    call_count += 1

    if not houses:
        return 0
    if len(houses) == 1:
        return houses[0]

    dp = [0]*len(houses)
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i-2]+houses[i], dp[i-1])

    return dp[len(houses)-1]


call_count = 0
result1 = recurse_counted(len(houses)-1)
print(f"Naive recursion: {result1}, function calls: {call_count}")

call_count_arr = [0]
result2 = memoization_counted(houses, call_count_arr)
print(f"memoization: {result2}, function calls: {call_count_arr[0]}")

call_count = 0
result3 = tabulation_counted(houses)
print(f"tabulation: {result3}, function calls: {call_count}")
