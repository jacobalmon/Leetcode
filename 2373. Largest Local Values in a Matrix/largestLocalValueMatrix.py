class Solution(object):
    def countLargest(self, grid, col, row):
        max_value = 0
        
        for i in range(col, col + 3):
            for j in range(row, row + 3):
                max_value = max(max_value, grid[i][j])

        return max_value

    def largestLocal(self, grid):
        n = len(grid)
        m = n -2

        mat = [[0] * m for _ in range(m)]

        for col in range(m):
            for row in range(m):
                mat[col][row] = self.countLargest(grid, col, row)

        return mat
