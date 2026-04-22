class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        R = len(matrix); C = len(matrix[0])
        dp = {} # (r, c) -> LIP

        def dfs(r, c, prevVal):
            if (r < 0 or r == R or
                c < 0 or c == C or
                matrix[r][c] <= prevVal): return 0

            if (r, c) not in dp:
                # dp[(r, c)] = 1
                for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    dp[(r, c)] = max(dp.get((r, c), 1), 1 + dfs(r + dr, c + dc, matrix[r][c]))
            
            return dp[(r, c)]

        for r in range(R):
            for c in range(C):
                dfs(r, c, -1)
                
        return max(dp.values())