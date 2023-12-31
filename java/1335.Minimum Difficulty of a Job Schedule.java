class Solution {
    public int minDifficulty(int[] jobDifficulty, int d) {
        return dpHelper(jobDifficulty, d);
    }

    public int dpHelper(int[] jobDifficulty, int d) {
        int n = jobDifficulty.length;
        if (n < d) {
            return -1;
        }
        float[][] dp = new float[n + 1][d + 1];

        for (float[] row : dp) {
            Arrays.fill(row,Integer.MAX_VALUE);
        }
        dp[0][0] = 0;
        for (int i = 1; i < n + 1; i++) {
            for (int j = 1; j < d + 1; j++) {
                int max_diff = 0;
                for (int k = i; k > 0; k--) {
                    max_diff = Math.max(max_diff, jobDifficulty[k - 1]);
                    dp[i][j] = Math.min(dp[i][j], dp[k - 1][j - 1] + max_diff);
                }
            }
        }

        return dp[n][d] == Integer.MAX_VALUE ? -1 : (int) dp[n][d];
    }
}
