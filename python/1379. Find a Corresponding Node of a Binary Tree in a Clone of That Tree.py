#Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def helper(orig, clone, target):
            if orig == None or clone == None:
                return None
            elif orig == target:
                return clone
            leftResult = helper(orig.left,clone.left,target)
            if leftResult == None:
                return helper(orig.right,clone.right,target)
            return leftResult
        return helper(original, cloned, target)