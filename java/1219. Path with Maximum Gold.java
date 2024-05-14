// Time Complexity: O(m*n*4^g) where m is the number of columns in grid, n is the number of rows in the grid, and g is the number of cell with gold in it. The algorithm uses nested for loop, traversing every cell in the m by n matrix. If there is gold in the cell, recursively the adjacent cells, left, right, up, and down, are explored, in worst case branching factor of 4 and having 4^g time.
// Space Complexity: O(g), the space complexity is determined by the depth of the recursion stack, which is the path through the cells with gold, which is g.
class Solution {
    public int getMaximumGold(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;
        int maxCollected = 0;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                maxCollected = Math.max(maxCollected,helper(grid,i,j,m,n,0));
            }
        }
        return maxCollected;
    }
    public int helper(int[][] grid, int i, int j, int m, int n, int collectedGold){
        if(i < 0 || j < 0 || i >= m || j >= n || grid[i][j] == 0){
            return collectedGold;
        }
        int originalGrid = grid[i][j];
        int newCollected = originalGrid + collectedGold;
        grid[i][j] = 0;
        int up = helper(grid,i-1,j,m,n,newCollected);
        int down = helper(grid,i+1,j,m,n,newCollected);
        int left = helper(grid,i,j-1,m,n,newCollected);
        int right = helper(grid,i,j+1,m,n,newCollected);
        grid[i][j] = originalGrid;
        return Math.max(Math.max(up,down), Math.max(left,right));
    }
}