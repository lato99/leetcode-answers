# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

# First solution - with recursion
# Time Complexity: In the algorithm, each node is visited once, and in each iteration constant time O(1)of work is done. At each iteration, it is checked if it is leaf node, and if it is left child or not. The whole tree will be traversed, which is O(n) time, then at each traverse, O(1) time amount of work will be done. So the overall time complexity is O(n).
# Space Complexity: The maximum numbers of function calls on hte call stack corresponds to the depth of the binary tree. In worst case scenario, where the binary tree is completely unbalanced, the recursion depth would be O(n), where n is the number of nodes in the tree. Additionally, since there are no additional data structures being used other than the call stack, the overall space complexity is O(n). Or in other words, the space complexity is O(H), where H is the height of the binary tree. Since the space complexity is determined by the recursion stack.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.helper(root,False)
    def helper(self, root, isLeft):
        if not root:
            return 0
        if root.left == None and root.right == None:
            if isLeft:
                return root.val
            return 0
        return self.helper(root.left,True) + self.helper(root.right,False)
        

#Second solution - again recursion, with better perfromanced algorithm, both in time and space complexity.
#Time Complexity: The algorithm traverse every node in the tree with recursion, and does constant time in each traverse. When compared to first solution, it checks the left child if it is left leaf, if so it avoids unnecessary recursive calls.
#Space Comlexity: The recursion stack is O(n) in worst case. However, it has better performance than the first solution, because it avoids redundant recursion calls.
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        else:
            if root.left:
                if not root.left.left and not root.left.right :
                    return root.left.val + self.sumOfLeftLeaves(root.right)
                else:
                    return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            return self.sumOfLeftLeaves(root.right)