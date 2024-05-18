# Time Complexity : O(n), where n is the number of nodes. The algorithm traverses each node once, and does constant time operation on each traverse.
# Space Complexity : O(n), where n is the number of nodes. There is no extra data structure, the space complexity is determined by the recursion stack. In worst case, the recursion stack can be O(n) when all the nodes have only left or right child, where it is a skewed binary tree.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        def countMoves(root):
            if root == None:
                return 0
            left = countMoves(root.left)
            right = countMoves(root.right)
            self.moves = self.moves + abs(left) + abs(right)
            return root.val - 1 + left + right
        countMoves(root)
        return self.moves