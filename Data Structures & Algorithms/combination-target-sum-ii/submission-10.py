class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        n = len(candidates)

        def dfs(i, total):
            if total == target:
                res.append(path.copy())
                return
            if (i == n or
                total > target):
                return

            path.append(candidates[i])
            dfs(i + 1, total + candidates[i])
            path.pop()

            # skip all same candidates
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res