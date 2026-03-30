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

            leftMaxDown, leftBest = dfs(root.left)
            rightMaxDown, rightBest = dfs(root.right)

            # leftMaxDown = max(leftMaxDown, 0)
            # rightMaxDown = max(rightMaxDown, 0)

            maxDown = root.val + max(leftMaxDown, rightMaxDown)
            throughRoot = root.val + leftMaxDown + rightMaxDown
            best = max(leftBest, rightBest, throughRoot)

            return max(maxDown, 0), best

        return dfs(root)[1]
