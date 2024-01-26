class Solution {
    public int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        int[][][] dp = new int[m][n][maxMove+1];
        for(int i = 0; i < m; i++){
            for(int j = 0 ; j < n ; j++){
                for(int z = 0; z < maxMove+1; z++){
                    dp[i][j][z] = -1;
                }
            }
        }
        return helper(dp,m,n,maxMove,startRow,startColumn);
    }
    public int helper(int[][][] dp, int m, int n,int maxMove,int startRow, int startColumn){
        if(startRow < 0 || startColumn < 0 || startRow >= m || startColumn >= n){
            return 1;
        }
        else if(maxMove == 0){
            return 0;
        }
        else if(dp[startRow][startColumn][maxMove] != -1){
            return dp[startRow][startColumn][maxMove];
        }
        else{
            long up = (long) helper(dp,m,n,maxMove-1,startRow-1,startColumn)  % (long) (Math.pow(10,9) + 7);
            long down = (long) helper(dp,m,n,maxMove-1,startRow+1,startColumn)  %  (long) (Math.pow(10,9) + 7);
            long left = (long) helper(dp,m,n,maxMove-1,startRow,startColumn-1)  %  (long) (Math.pow(10,9) + 7);
            long right = (long) helper(dp,m,n,maxMove-1,startRow,startColumn+1) %  (long) (Math.pow(10,9) + 7);
            long temp = (long) (up + down + left + right) %  (long) (Math.pow(10,9) + 7);
            dp[startRow][startColumn][maxMove] = (int) temp;
            return dp[startRow][startColumn][maxMove];
        }
    }
}

// Time Complexity is O(n*m*maxMove) : The algorithm initializes the dp[m][n][maxMove] array which takes O(m*n*maxMove) time. The helper function recursively calls itself for up,down,left,right moves on the grid. The max depth of the recursion is maxMove, and it can be called for every index on the grid m*n. So it takes O(m*n*maxMove) time if every location is visited in the grid.
// Space Complexity is O(n*m*maxMove) : The space is used by dp array, which has the size O(m*n*maxMove). The call stack uses O(maxMove) space because the recursive calls can be up to maxMove time at most.