grid = [[1,3],
        [2,2]]

n = len(grid)**2
expected_sum = (n*(n+1)) // 2
expected_squ_sum = (n*(n+1)*(2*n + 1)) // 6


actual_sum = 0
acutal_squ_sum = 0
for i in range(len(grid)):
    for j in range(len(grid[i])):
        actual_sum += grid[i][j]
        acutal_squ_sum += grid[i][j]**2



#x-y = expected_sum - actual_sum
diff_x_y = expected_sum-actual_sum
#(x+y)(x-y) = (expected_sum**2) - (actual_sum**2)
diff_x2_y2 = (expected_squ_sum- acutal_squ_sum)
#x+y = ((expected_sum**2) - (actual_sum**2))//x-y
add_x_y = diff_x2_y2//diff_x_y

#calculate y , then replace x for expected_sum - actual_sum + y
#itll become (x-y)+y+y = x+y
#2y = x+y - (x-y)
#y = ((x+y)-(x-y))//2

y = (add_x_y - diff_x_y)//2
x = diff_x_y + y



