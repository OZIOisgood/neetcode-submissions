class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        path = []
        def dfs(opened, closed):
            if opened > n: return
            if closed > opened: return
            if opened == n and closed == n:
                res.append("".join(path))
                return
            
            path.append('(')
            dfs(opened + 1, closed)
            path.pop()
            
            path.append(')')
            dfs(opened, closed + 1)
            path.pop()
        dfs(0, 0)
        return res