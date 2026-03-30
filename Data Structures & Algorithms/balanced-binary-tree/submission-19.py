# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node: return [True, 0]
            lB, lV = dfs(node.left)
            rB, rV = dfs(node.right)
            return [lB and rB and abs(lV - rV) <= 1, 1 + max(lV, rV)]
        
        return dfs(root)[0]