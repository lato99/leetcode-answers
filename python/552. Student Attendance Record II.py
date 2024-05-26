# Time Complexity : O(n). The helper function is called for every possible case of present,late, and absent for n days. In total it is called n*3*2 = 6n times, resulting in O(n) time.
# Space Complexity : O(n). The call stack from recursion is at most O(n). For memoization, 3D array has space O(6n) which is O(n). Thus the overall space complexity is O(n).
class Solution:
    def checkRecord(self, n: int) -> int:
        memo = [[[-1] * 3 for _ in range(2)] for _ in range(n+1)]
        return self.helper(n,0,0,memo)
    def helper(self, n , absentDays, lateDays, memo):
        mod = (10 ** 9) + 7
        if absentDays >= 2 or lateDays >= 3:
            return 0
        if n == 0:
            return 1
        if memo[n][absentDays][lateDays] != -1:
            return memo[n][absentDays][lateDays]
        else:
            count = self.helper(n-1,absentDays,0,memo)
            count %= mod
            count += self.helper(n-1,absentDays+1,0,memo) 
            count %= mod
            count += self.helper(n-1,absentDays,lateDays+1,memo)
            count %= mod
            memo[n][absentDays][lateDays] = count
            return memo[n][absentDays][lateDays]