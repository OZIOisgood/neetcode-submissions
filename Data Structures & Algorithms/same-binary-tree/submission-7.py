# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        

        if (
            (not q and p)
            or (q and not p)
            or p.val != q.val
            or not self.isSameTree(p.left, q.left)
            or not self.isSameTree(p.right, q.right)):
            return False
        return True