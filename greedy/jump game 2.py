def jump(nums: list[int]) -> int:  # type:ignore

    if len(nums) == 1:
        return 0
    jumps = 0
    next_max = 0
    curr_max = 0
    for idx, num in enumerate(nums):
        next_max = max(next_max, idx+num)
        if idx == curr_max:
            jumps += 1
            curr_max = next_max

        if curr_max >= len(nums)-1:
            return jumps


nums = [0]
print(jump(nums))
