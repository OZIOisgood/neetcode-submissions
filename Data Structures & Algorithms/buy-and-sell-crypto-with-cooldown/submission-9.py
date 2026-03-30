class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}  # (i, buying): max_profit
        def dfs(i, buying):
            if i >= len(prices): return 0
            if (i, buying) not in dp:
                cooldown = dfs(i + 1, buying)
                if buying: profit = dfs(i + 1, not buying) - prices[i] # buy
                else: profit = dfs(i + 2, not buying) + prices[i] # sell
                dp[(i, buying)] = max(profit, cooldown)
            return dp[(i, buying)]
        return dfs(0, True)