# Time Complexity: O(m*n*4^g) where m is the number of columns in grid, n is the number of rows in the grid, and g is the number of cell with gold in it. The algorithm uses nested for loop, traversing every cell in the m by n matrix. If there is gold in the cell, recursively the adjacent cells, left, right, up, and down, are explored, in worst case branching factor of 4 and having 4^g time.
# Space Complexity: O(g), the space complexity is determined by the depth of the recursion stack, which is the path through the cells with gold, which is g.
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        maxCollected = 0
        m = len(grid)
        n = len(grid[0])
        def helper(grid, i, j, m, n, collectedGold):
            if i < 0 or j < 0 or i >= m or j>= n or grid[i][j] == 0:
                return collectedGold
            originalGrid = grid[i][j]
            totalGold = collectedGold + originalGrid
            grid[i][j] = 0
            up = helper(grid,i-1,j,m,n,totalGold)
            down = helper(grid,i+1,j,m,n,totalGold)
            left = helper(grid,i,j - 1,m,n,totalGold)
            right = helper(grid,i,j + 1,m,n,totalGold)
            grid[i][j] = originalGrid
            return max(up,down,left,right)
        for i in range(m):
            for j in range(n):
                maxCollected = max(maxCollected,helper(grid,i,j,m,n,0))
        return maxCollected