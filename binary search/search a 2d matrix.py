matrix = [[1, 3]]
target = 3


def searchMartix(matrix: list[list[int]], target: int):
    top = 0
    bottom = len(matrix)-1

    while top <= bottom:
        row = (top + bottom) // 2
        if target >= matrix[row][0] and target <= matrix[row][-1]:
            break
        elif target < matrix[row][0]:
            bottom = row - 1
        else:
            top = row + 1

    left = 0
    right = len(matrix[row])-1

    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return False


print(searchMartix(matrix, target))
