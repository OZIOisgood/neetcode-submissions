# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: return []
        q = deque([root])
        res = []
        while q:
            q_level_size = len(q)
            lvl = []
            for _ in range(q_level_size):
                node = q.popleft()
                lvl.append(node.val)
                for kid in [node.left, node.right]:
                    if kid != None:
                        q.append(kid)
            res.append(lvl)
        return res