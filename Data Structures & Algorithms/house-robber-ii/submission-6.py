class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        return max(self.help(nums[0:len(nums) - 1]),
                   self.help(nums[1:len(nums)]))

    def help(self, nums: List[int]) -> int:
        n = len(nums); dp = {n: 0, n + 1: 0}
        def dfs(i):
            if i not in dp: dp[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])
            return dp[i]
        return dfs(0)