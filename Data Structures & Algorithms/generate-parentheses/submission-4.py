class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        path = []; res = []
        def bt(opened, closed):
            if opened == closed == n:   res.append("".join(path)); return
            if opened < n:              path.append("("); bt(opened + 1,closed); path.pop()
            if closed < opened:         path.append(")"); bt(opened,closed + 1); path.pop()
        bt(0,0)
        return res