/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
// Time Complexity: O(n), we call the recursive funciton on every node once, and it takes O(1) time on each call, since there is 1 if else statement and 1 operation on each case.
// Space Complexity: O(log n): Since it is a full binary tree, if there are n nodes, the height of the tree will be log n. The space will be used by the recursion stack. Since it is a recursive algorithm, and the nodes recursively call their children before return statement, in worst case the recursion stack can have height logn. Therefore the space complexity is O(n)
class Solution {
    public boolean evaluateTree(TreeNode root) {
        if(root.left == null && root.right == null){
            return root.val == 1;
        }
        else if(root.val == 2){
            return evaluateTree(root.left) || evaluateTree(root.right);
        }
            return evaluateTree(root.left) && evaluateTree(root.right);

    }
}