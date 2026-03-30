class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {n: 1, n + 1: 0}
        def dfs(i):
            if i not in dp: dp[i] = dfs(i + 1) + dfs(i + 2)
            return dp[i]
        return dfs(0)