class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        ROWS = len(board); COLS = len(board[0])
        DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        def dfs(r, c, cur_letter_idx):
            if cur_letter_idx == n: return True
            if not (0 <= r < ROWS and
                    0 <= c < COLS and
                    board[r][c] == word[cur_letter_idx]):
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            
            for dr, dc in DIRS:
                if dfs(r + dr, c + dc, cur_letter_idx + 1) == True:
                    board[r][c] = tmp
                    return True
            
            board[r][c] = tmp
            return False
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0) == True:
                    return True
        
        return False