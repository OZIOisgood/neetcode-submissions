class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums: return True

        totalSum = sum(nums); n = len(nums)
        if totalSum % 2 != 0: return False
        target = totalSum // 2

        dp = {}
        def dfs(i, total):
            if total == target: return True
            if total > target or i == n: return False

            if (i, total) not in dp:
                dp[(i, total)] = dfs(i + 1, total + nums[i]) or dfs(i + 1, total)

            return dp[(i, total)]
        
        return dfs(0, 0)