class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [dict() for _ in range(n)]
        ans = 0
        for i in range(1,n):
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[i]:
                    dp[i][diff] += 1
                else:
                    dp[i][diff] = 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    ans += dp[j][diff]
        return ans
    
#Time Complexity: O(n^2)
#Because of the nested loop. The outer loop iterates n times, and the inner loop iterates i times where i is the outer loop's current index. The operations inside the for loops are hashmap operations, which are O(1), therefore the dominant factor in Time Complexity is O(n^2)
#Space Complexity: O(n^2)
#The primary space usage is from the hashmap. We store the difference of the elements of every possible element in nums in the hashmap. If every element in the nums array has unique difference, then the hashmap will store O(n^2) in total. The size of the dp array is constant which is the length of the nums array. So the dominant factor in the space complexity is the space of hashmap, which is O(n^2) in the worst case.