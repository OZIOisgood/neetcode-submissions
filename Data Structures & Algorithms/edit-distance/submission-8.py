class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        COLS = len(word1); ROWS = len(word2)
        dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]

        for c in range(COLS + 1):
            dp[ROWS][c] = COLS - c
        for r in range(ROWS + 1):
            dp[r][COLS] = ROWS - r

        for r in range(ROWS - 1, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if word1[c] == word2[r]:
                    dp[r][c] = dp[r + 1][c + 1]
                else:
                    dp[r][c] = 1 + min(
                        dp[r + 1][c],       # delete
                        dp[r][c + 1],       # insert
                        dp[r + 1][c + 1]    # replace
                    )
        
        return dp[0][0]