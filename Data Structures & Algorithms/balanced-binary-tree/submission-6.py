# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode]) -> tuple[int, bool]:
            if node:
                left = dfs(node.left)
                right = dfs(node.right)

                return (
                    max(
                        left[0],
                        right[0]
                    ) + 1,
                    left[1] and right[1] and abs(left[0] - right[0]) <= 1
                )
            else:
                return (0, True)
        

        return dfs(root)[1]