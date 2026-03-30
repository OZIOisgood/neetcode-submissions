class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == C or board[r][c] != "O": return

            board[r][c] = "T"
            for dr, dc in dirs: dfs(r + dr, c + dc)

        for r in range(R):
            if board[r][0] == "O": dfs(r, 0)
            if board[r][C - 1] == "O": dfs(r, C - 1)

        for c in range(C):
            if board[0][c] == "O": dfs(0, c)
            if board[R - 1][c] == "O": dfs(R - 1, c)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O": board[r][c] = "X"
                if board[r][c] == "T": board[r][c] = "O"
