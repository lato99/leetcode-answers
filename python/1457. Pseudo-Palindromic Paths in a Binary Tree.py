# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from pyparsing import Optional


class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.dpHelper(root, set())
    def dpHelper(self, root, frequencySet):
        if root == None:
            return 0
        else:
            frequencySetCopy = frequencySet.copy()
            if root.val in frequencySet:
                frequencySetCopy.remove(root.val)
            else:
                frequencySetCopy.add(root.val)
            if (root.left == None and root.right == None):
                return 1 if len(frequencySetCopy) <= 1 else 0
            else:
                return self.dpHelper(root.left, frequencySetCopy) + self.dpHelper(root.right, frequencySetCopy)