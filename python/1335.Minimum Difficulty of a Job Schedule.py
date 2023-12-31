class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        return self.dp(jobDifficulty,d)
    def dp(self, jobDifficulty: List[int], d:int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[float("inf")]* (d+1) for i in range(n+1)]
        dp[0][0] = 0 #0 jobs in 0 days is 0 difficulty
        for jobIndex in range(1,n+1):
            for dayIndex in range(1,d+1):
                max_diff = 0
                for k in range(jobIndex, 0, -1):
                    max_diff = max(max_diff, jobDifficulty[k-1])
                    dp[jobIndex][dayIndex] = min(dp[jobIndex][dayIndex], max_diff+dp[k-1][dayIndex-1])
        if dp[n][d] == float("inf"):
            return -1
        return dp[n][d]
