class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r, maxProfit= 0, 1, 0
        while r < len(prices):
            if prices[l] < prices[r]: maxProfit = max(maxProfit, prices[r] - prices[l])
            else: l = r
            r += 1
        return maxProfit