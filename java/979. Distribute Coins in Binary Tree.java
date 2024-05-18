// Time Complexity : O(n), where n is the number of nodes. The algorithm traverses each node once, and does constant time operation on each traverse.
// Space Complexity : O(n), where n is the number of nodes. There is no extra data structure, the space complexity is determined by the recursion stack. In worst case, the recursion stack can be O(n) when all the nodes have only left or right child, where it is a skewed binary tree.
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
class Solution {
    public int totalMoves = 0;
    public int distributeCoins(TreeNode root) {
        helper(root);
        return totalMoves;
    }
    public int helper(TreeNode root){
        if(root == null){
            return 0;
        }
        int left = helper(root.left);
        int right = helper(root.right);
        totalMoves += Math.abs(left) + Math.abs(right);
        return root.val -1 +left +right;
    }
}