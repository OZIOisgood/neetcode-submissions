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

            leftWithoutSplit, leftWithSplit = dfs(root.left)
            rightWithoutSplit, rightWithSplit = dfs(root.right)

            withoutSplit = root.val + max(0, leftWithoutSplit, rightWithoutSplit)
            withSplit = max(
                leftWithSplit,
                rightWithSplit,
                root.val + max(0, leftWithoutSplit) + max(0, rightWithoutSplit),
            )

            return withoutSplit, withSplit

        return dfs(root)[1]
