# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root and (not root.left and not root.right): return 0
        res = 0
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            nonlocal res
            res = max(res, r + l)
            return 1 + max(l, r)
        dfs(root)
        return res
