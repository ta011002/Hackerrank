"""
Problem : DFS: Connected Cell in a Grid
Explain : https://www.hackerrank.com/challenges/ctci-connected-cell-in-a-grid/problem
Input : Integer, n, denoting the number of rows in the matrix.
        Integer, m, denoting the number of columns in the matrix.
        Space-separated integers describing the respective values filling each row in the matrix.
Output : Print the number of cells in the largest region in the given matrix.
"""


def getBiggestRegion(grid):
    def getregion(grid, row, col):
        count = 0
        if (row not in range(len(grid))) or (col not in range(len(grid[0]))) or grid[row][col] == 0:
            return 0
        elif (row in range(len(grid))) and (col in range(len(grid[0]))) and (grid[row][col] == 1):
            count += 1
            grid[row][col] = 0
        count += getregion(grid, (row-1), (col-1))
        count += getregion(grid, (row  ), (col-1))
        count += getregion(grid, (row+1), (col-1))
        count += getregion(grid, (row-1), (col  ))
        count += getregion(grid, (row+1), (col  ))
        count += getregion(grid, (row-1), (col+1))
        count += getregion(grid, (row  ), (col+1))
        count += getregion(grid, (row+1), (col+1))
        count += getregion(grid, (row+1), (col+1))
        return count

    big_region = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            big_region.append(getregion(grid, i, j))
    return max(big_region)


n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)
print(getBiggestRegion(grid))
