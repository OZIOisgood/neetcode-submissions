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

            withoutSplit = root.val + max(0, l, r)
            withSplit = max(
                lS,
                rS,
                root.val + max(0, l) + max(0, r),
            )

            return withoutSplit, withSplit

        return dfs(root)[1]
