import java.util.HashMap;

class Solution {
    public int numberOfArithmeticSlices(int[] nums) {
        long ans = 0;
        int n = nums.length;
        HashMap<Long, Long>[] dp = new HashMap[n];
        for(int i = 0; i < n; i++){
            dp[i] = (new HashMap<Long,Long>());
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < i; j++){
                long diff = (long) nums[i] - nums[j];
                dp[i].put(diff,dp[i].getOrDefault(diff,0L)+1);
                if(dp[j].containsKey(diff)){
                    dp[i].put(diff,dp[i].getOrDefault(diff,0L)+dp[j].get(diff));
                    ans += dp[j].get(diff);
                }
            }
        }
        return (int) ans;

    }
}

// Time Complexity: O(n^2)
// Because of the nested loop. The outer loop iterates n times, and the inner loop iterates i times where i is the outer loop's current index. The operations inside the for loops are hashmap operations, which are O(1), therefore the dominant factor in Time Complexity is O(n^2)
// Space Complexity: O(n^2)
// The primary space usage is from the hashmap. We store the difference of the elements of every possible element in nums in the hashmap. If every element in the nums array has unique difference, then the hashmap will store O(n^2) in total. The size of the dp array is constant which is the length of the nums array. So the dominant factor in the space complexity is the space of hashmap, which is O(n^2) in the worst case.