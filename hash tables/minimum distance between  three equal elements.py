matrix = [[1, 2], [1, 3]]


def kthSmallest(matrix, k):

    def count(mid):
        counter = 0
        # start at bottom left , go to top right
        # matrix[rows-1][0] to matrix[0][cols-1]
        # check if that element is smaller or equal to mid
        # if so then add everything above in that colum and move to right,
        # if not then move up one row and check again
        index_x = len(matrix)-1
        index_y = 0
        while index_x >= 0 and index_y <= len(matrix[0])-1:
            if matrix[index_x][index_y] <= mid:
                counter += index_x+1
                index_y += 1
            else:
                index_x -= 1
        return counter

    left = matrix[0][0]
    right = matrix[len(matrix)-1][len(matrix[0])-1]
    counter = 0
    mid = 0
    while left <= right:
        mid = (left+right) // 2
        counter = count(mid)
        if counter < k:
            left = mid + 1
        else:
            right = mid - 1

    return left


print(kthSmallest(matrix, 3))
