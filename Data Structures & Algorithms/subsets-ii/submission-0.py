class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                print(tuple(subset))
                res.add(tuple(subset))
                return

            # /
            backtrack(i + 1, subset + [nums[i]])

            # \
            backtrack(i + 1, subset)

        backtrack(0, [])
        return [list(s) for s in res]