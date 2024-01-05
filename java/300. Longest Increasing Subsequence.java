import java.util.Arrays;

class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        Arrays.fill(dp,1);
        for(int i = 1; i < n ; i++){
            for(int j = 0; j < i; j++){
                int iVal = nums[i];
                int jVal = nums[j];
                if(iVal > jVal){
                    dp[i] = Math.max(dp[i],dp[j]+1);
                }
            }
        }
        int ans = dp[0];
        for(int i = 1; i < n; i++){
            if(dp[i] > ans){
                ans = dp[i];
            }
        }
        return ans;
    }
}