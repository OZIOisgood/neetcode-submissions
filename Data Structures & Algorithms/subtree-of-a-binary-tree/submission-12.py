# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, tree: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not sub: return True
        if not tree and sub: return False
        if self.sameTree(tree, sub): return True
        return (self.isSubtree(tree.left, sub) or
                self.isSubtree(tree.right, sub))
    
    def sameTree(self, tree: Optional[TreeNode], sub: Optional[TreeNode]) -> bool:
        if not tree and not sub: return True
        if tree and sub and tree.val == sub.val:
            return (self.sameTree(tree.left, sub.left) and
                    self.sameTree(tree.right, sub.right))
        return False