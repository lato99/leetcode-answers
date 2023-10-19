/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {

    public class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode(int x) { val = x; }
    }

    public final TreeNode getTargetCopy(final TreeNode original, final TreeNode cloned, final TreeNode target) {
        return helper(original, cloned, target);
        
    }
    public TreeNode helper(TreeNode orig, TreeNode clone, TreeNode target){
        if(orig == null || clone == null){
            return null;
        }
        if(orig == target){
            return clone;
        }
        TreeNode leftResult = helper(orig.left, clone.left, target);
        return (leftResult == null) ? helper(orig.right,clone.right, target) : leftResult;
    }
    
}