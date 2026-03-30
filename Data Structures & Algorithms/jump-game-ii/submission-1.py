class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        target = n - 1
        dp = [float('inf')] * n
        dp[target] = 0

        for i in range(target - 1, -1, -1):
            furthest = min(target, i + nums[i])
            for j in range(i + 1, furthest + 1):
                dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]