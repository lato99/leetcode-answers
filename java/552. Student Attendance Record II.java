// Time Complexity : O(n). The helper function is called for every possible case of present,late, and absent for n days. In total it is called n*3*2 = 6n times, resulting in O(n) time.
// Space Complexity : O(n). The call stack from recursion is at most O(n). For memoization, 3D array has space O(6n) which is O(n). Thus the overall space complexity is O(n).

class Solution {
    public int checkRecord(int n) {
        int[][][] memo = new int[n+1][3][2]; 
        for(int i = 0; i < n+1; i++){
            for(int j = 0; j < 3; j++){
                for(int k = 0; k < 2; k++){
                    memo[i][j][k] = -1;
                }
            }
        }
        return helper(n,memo,0,0);
    }
    public int helper(int n, int[][][] memo, int lateDays, int absentDays){
        int mod = 1000000007;
        if(absentDays > 1 || lateDays > 2){
            return 0;
        }
        else if(n == 0){
            return 1;
        }
        if(memo[n][lateDays][absentDays] != -1){
            return memo[n][lateDays][absentDays];
        }
        int count = helper(n-1,memo,0,absentDays); //Present Case
        count %= mod;
        count += helper(n-1, memo, 0, absentDays+1); //Absent Case
        count %= mod;
        count += helper(n-1,memo,lateDays+1,absentDays); //Late Case
        count %= mod;
        memo[n][lateDays][absentDays] = count;
        return count;
    }
}