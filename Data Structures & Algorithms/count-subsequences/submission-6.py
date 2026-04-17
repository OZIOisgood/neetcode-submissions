class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = {}
        def dfs(i, j):
            if j == len(t): return 1
            if i == len(s): return 0
            if (i, j) not in dp:
                dp[(i, j)] = dfs(i + 1, j) + (dfs(i + 1, j + 1) if s[i] == t[j] else 0)
            return dp[(i, j)]
        return dfs(0,0)