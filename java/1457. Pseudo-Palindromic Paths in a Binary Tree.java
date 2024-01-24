
// Definition for a binary tree node.

import java.util.HashSet;

class Solution {
       public class TreeNode {
       int val;
       TreeNode left;
       TreeNode right;
       TreeNode() {}
       TreeNode(int val) { this.val = val; }
       TreeNode(int val, TreeNode left, TreeNode right) {
           this.val = val;
           this.left = left;
           this.right = right;
       }
   }
    public int pseudoPalindromicPaths (TreeNode root) {
        return helper(root, new HashSet<Integer>());
    }
    public int helper(TreeNode root, HashSet<Integer> hs){
        if(root == null){
            return 0;
        }
        HashSet<Integer> hsCopy = new HashSet<Integer>(hs);
        if(hs.contains(root.val)){
            hsCopy.remove(root.val);
        }
        else{
            hsCopy.add(root.val);
        }
        if(root.left == null && root.right == null){
        if(hsCopy.size() > 1){
            return 0;
        } else {
            return 1;
        }
        }
        return helper(root.left,hsCopy) + helper(root.right,hsCopy);
    }

}