class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, total):
            if amount == total: return 1
            if i == len(coins) or total > amount: return 0
            if (i, total) not in dp: dp[(i, total)] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return dp[(i, total)]
        return dfs(0, 0)