class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums); res = []; path = []
        def dfs(i, total):
            if i == n or total > target: return
            if total == target:
                res.append(path.copy())
                return
            
            # continue with the same value
            path.append(nums[i])
            dfs(i, total + nums[i])
            path.pop()

            # proceed with the next value
            dfs(i + 1, total)

        dfs(0, 0)
        return res