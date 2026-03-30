# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return max(
            self.maxDepth(root.left),
            self.maxDepth(root.right)
        ) + 1 if root else 0
        # O(n) time and O(h) space complexity
        # Best case - O(log(n))    balanced tree      0=8
        # Worst case - O(n)        degenerate tree    0-0-0