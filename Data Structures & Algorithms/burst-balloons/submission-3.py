class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        dp = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) not in dp:
                for i in range(l, r + 1):
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dfs(l, i - 1) + dfs(i + 1, r)
                    dp[(l, r)] = max(dp.get((l, r), 0), coins)

            return dp[(l, r)]

        return dfs(1, len(nums) - 2)