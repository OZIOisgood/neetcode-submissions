class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.add(tuple(subset))
                return

            # /
            backtrack(i + 1, subset + [nums[i]])

            # skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # \
            backtrack(i + 1, subset)

        backtrack(0, [])
        return [list(s) for s in res]