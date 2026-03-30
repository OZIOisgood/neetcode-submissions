class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        ROWS = len(board); COLS = len(board[0])
        
        # mark border regions
        def dfs(r, c):
            if (0 <= r < ROWS and
                0 <= c < COLS and
                board[r][c] == 'O'):
                board[r][c] = 'BR'
                for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    dfs(r + dr, c + dc)
        
        # for each cell in the border we run dfs
        for r in range(ROWS):
            for c in range(COLS):
                if ((r == 0 or r == ROWS - 1 or
                     c == 0 or c == COLS - 1) and
                    board[r][c] == 'O'):
                    dfs(r, c)
        
        # change all 'O' to 'X' and all 'BR' to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':  board[r][c] = 'X'
                if board[r][c] == 'BR': board[r][c] = 'O'