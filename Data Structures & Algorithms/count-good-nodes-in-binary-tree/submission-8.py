# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, MAX):
            if not node: return 0
            NEW_MAX = max(node.val, MAX)
            l = dfs(node.left, NEW_MAX)
            r = dfs(node.right, NEW_MAX)
            return (1 if node.val >= MAX else 0) + l + r
        return dfs(root, float("-inf"))