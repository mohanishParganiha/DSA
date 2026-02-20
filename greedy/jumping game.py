def jumpGame(nums: list[int]) -> bool:
    max_reach = 0
    for idx, num in enumerate(nums):
        if idx > max_reach:
            return False
        max_reach = max(max_reach, idx+num)
        if max_reach >= len(nums)-1:
            return True
    return True


list_of_nums_list = [[2, 2, 0], [3, 2, 1, 0, 4],
                     [0], [1], [2, 0], [1, 1, 1, 1], [0, 1]]
for nums_list in list_of_nums_list:
    print(f"list:{nums_list} ans:{jumpGame(nums_list)}")
