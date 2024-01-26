class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        l = max(m,n,maxMove)
        dp = [[[-1] * (maxMove + 1) for _ in range(n)] for __ in range(m)]
        return self.helper(m,n,maxMove,startRow,startColumn,dp) 
    def helper(self, m,n,maxMove,sR,sC,dp):
        if sR<0 or sR >= m or sC < 0 or sC >= n :
            return 1
        if maxMove <= 0:
            return 0
        elif dp[sR][sC][maxMove] != -1:
            return dp[sR][sC][maxMove]
        else:
            up = self.helper(m,n,maxMove-1,sR-1,sC,dp)
            down = self.helper(m,n,maxMove-1,sR+1,sC,dp)
            left = self.helper(m,n,maxMove-1, sR,sC-1,dp)
            right = self.helper(m,n,maxMove-1,sR,sC+1,dp)
            dp[sR][sC][maxMove] = (up+down+left+right) % (pow(10,9)+7)
            return dp[sR][sC][maxMove]
# Time Complexity is O(n*m*maxMove) : The algorithm initializes the dp[m][n][maxMove] array which takes O(m*n*maxMove) time. The helper function recursively calls itself for up,down,left,right moves on the grid. The max depth of the recursion is maxMove, and it can be called for every index on the grid m*n. So it takes O(m*n*maxMove) time if every location is visited in the grid.
# Space Complexity is O(n*m*maxMove) : The space is used by dp array, which has the size O(m*n*maxMove). The call stack uses O(maxMove) space because the recursive calls can be up to maxMove time at most.