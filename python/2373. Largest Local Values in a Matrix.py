# Time Complexity : O(n*n) where n is the length of input list grid. First the algorithm gets in a nested for loop, both inner and outer loop iterates over n-2 time, iterating over the grid. helper function is called in the inner loop, which also has nested loop, but constant time. So overall time complexity is O(n*n)
# Space Complexity : O(1), constant space
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[-1] * (n-2) for i in range(n-2)]
        for i in range(1,n-1):
            for j in range(1,n-1):
                maxLocal[i-1][j-1] = self.helper(grid,i,j)
        return maxLocal
    def helper(self, arr, i,j):
        ret = -1
        for x in range(i-1,i+2):
            for y in range(j-1,j+2):
                ret = max(ret,arr[x][y])
        return ret
0