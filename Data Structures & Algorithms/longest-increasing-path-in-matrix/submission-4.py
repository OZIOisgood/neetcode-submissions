class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dp = {}  # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or matrix[r][c] <= prevVal
            ):
                return 0

            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = 1
            for d in directions:
                dp[(r, c)] = max(
                    dp[(r, c)],
                    1 + dfs(
                        r + d[0],
                        c + d[1],
                        matrix[r][c]
                    )
                )
            
            return dp[(r, c)]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
                
        return max(dp.values())