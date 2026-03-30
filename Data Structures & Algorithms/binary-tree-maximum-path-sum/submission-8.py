# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return 0, float("-inf")

            l, lS = dfs(root.left)
            r, rS = dfs(root.right)

            withoutSplit = root.val + max(l, r)
            cS = root.val + l + r
            withSplit = max(lS, rS, cS)

            return max(0, withoutSplit), withSplit

        return dfs(root)[1]
