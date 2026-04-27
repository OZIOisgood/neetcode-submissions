class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posD = set()
        negD = set()

        res = []
        board = [["."] * n for i in range(n)]
        def bt(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if (c in cols
                    or (r + c) in posD
                    or (r - c) in negD):
                    continue
                
                cols.add(c)
                posD.add(r + c)
                negD.add(r - c)
                board[r][c] = "Q"

                bt(r + 1)
                
                cols.remove(c)
                posD.remove(r + c)
                negD.remove(r - c)
                board[r][c] = "."

        bt(0)
        return res