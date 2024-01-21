from ast import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # rob current, jump2
        # dont rob current, jump1
        n = len(nums)
        dp = [-1 for i in range(n)]
        return self.helper(nums,0,dp)
    def helper(self, nums, i,dp):
        if i>=len(nums):
            return 0
        elif dp[i] != -1:
            return dp[i]
        robCurr = nums[i] + self.helper(nums,i+2,dp)
        notRobCurr = self.helper(nums,i+1,dp)
        dp[i]=max(robCurr,notRobCurr)
        return dp[i]