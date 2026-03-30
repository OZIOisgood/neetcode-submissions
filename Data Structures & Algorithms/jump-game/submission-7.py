class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = {n - 1: True}

        def dfs(i):
            if i not in dp:
                dp[i] = False
                for j in range(1, nums[i] + 1):
                    if i + j < n:
                        dp[i] |= dfs(i + j)

            return dp[i]

        return dfs(0)