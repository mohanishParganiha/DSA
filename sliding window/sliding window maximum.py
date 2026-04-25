from collections import deque
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 2


def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    monotonic_que = deque()
    sol = []

    for i in range(len(nums)):
        while monotonic_que and nums[monotonic_que[-1]] <= nums[i]:
            monotonic_que.pop()

        if not monotonic_que or nums[monotonic_que[-1]] > nums[i]:
            monotonic_que.append(i)
            if monotonic_que[0] == i - k:
                monotonic_que.popleft()
            if i+1-k >= 0 and i-k-1 <= monotonic_que[0] <= i:
                sol.append(nums[monotonic_que[0]])

    return sol


print(maxSlidingWindow(nums, k))
