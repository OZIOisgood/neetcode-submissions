class Solution:
    def numSquares(self, n: int) -> int:
        dp = defaultdict(lambda: n)
        dp[0] = 0

        for target in range(1, n + 1):
            for s in range(1, target + 1):
                square = s * s
                if square > target: break
                dp[target] = min(dp[target], 1 + dp[target - square])

        return dp[n]