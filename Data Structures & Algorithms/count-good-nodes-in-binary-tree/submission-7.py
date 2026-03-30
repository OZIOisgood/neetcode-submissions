# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, MIN):
            if not node: return 0
            NEW_MIN = max(node.val, MIN)
            l = dfs(node.left, NEW_MIN)
            r = dfs(node.right, NEW_MIN)
            return (1 if node.val >= MIN else 0) + l + r
        return dfs(root, float("-inf"))