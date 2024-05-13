# Time Copmlexity : O(m*n), we traverse the m by n grid with inner for loop, which takes O(n*m) time.
# Space Complexity : O(1), the algorithm uses constant space, m, n, and result variable which are all integers
class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        result = (1 << n-1) * m
        for j in range(1,n):
            sameBits = 0
            for i in range(m):
                curr = grid[i][j]
                if grid[i][0] == 0:
                    curr = 1 - curr
                sameBits += curr
            result += (1 << n-1-j) * max(sameBits, m - sameBits)
        return result