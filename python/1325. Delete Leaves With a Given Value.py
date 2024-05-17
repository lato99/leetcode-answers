#Solution 1
# Time Complexity : O(n) where n is the number of nodes. Each node is visited once with recursion. At each node, constant time O(1) operations are done. Therefore the overall time complexity is O(n).
# Space Complexity : O(n) where n is hte number of nodes. The space complexity is determined by the recursion stack. In worst case, the tree is linear, so recursion stack is O(n).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if self.helper(root,target):
            return None
        return root
    def helper(self,root,target):
        if root == None:
            return True
        left = self.helper(root.left,target)
        right = self.helper(root.right, target)
        if left:
            root.left = None
        if right:
            root.right = None
        if left and right and root.val == target:
            return True

#Solution 2 

# Time Complexity : O(n) where n is the number of nodes. Each node is visited once with recursion. At each node, constant time O(1) operations are done. Therefore the overall time complexity is O(n).
# Space Complexity : O(n) where n is hte number of nodes. The space complexity is determined by the recursion stack. In worst case, the tree is linear, so recursion stack is O(n).

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None:
            return None
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right, target)
        if root.left == None and root.right == None and root.val == target:
            return None
        return root