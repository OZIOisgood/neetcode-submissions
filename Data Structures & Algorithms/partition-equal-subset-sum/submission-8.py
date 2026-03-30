class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0: return False

        target = total // 2
        n = len(nums)
        dp = {} # (i, target)

        def dfs(i, target):
            if target == 0: return True
            if target < 0 or i == n: return False
            if (i, target) not in dp:
                dp[(i, target)] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))
            return dp[(i, target)]
            

        return dfs(0, target)