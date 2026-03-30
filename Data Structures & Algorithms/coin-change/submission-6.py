class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float("inf")
        dp = {}  # (i, total) -> min coins needed from here

        def dfs(i, total):
            if total == amount: return 0
            if total > amount or i == len(coins): return INF

            if (i, total) in dp: return dp[(i, total)]

            dp[(i, total)] = min(
                1 + dfs(i, total + coins[i]),   # reuse same coin
                dfs(i + 1, total)        # move to next coin
            )
            return dp[(i, total)]

        res = dfs(0, 0)
        return -1 if res == INF else res
