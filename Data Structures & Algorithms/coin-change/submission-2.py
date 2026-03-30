class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0: return 0
            if amount not in memo:
                memo[amount] = float("inf")
                for coin in coins:
                    if amount - coin >= 0:
                        memo[amount] = min(memo[amount], 1 + dfs(amount - coin))
            return memo[amount]
        minCoins = dfs(amount)
        return -1 if minCoins == float("inf") else minCoins